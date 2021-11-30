from __future__ import print_function, division
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np 
import torchvision
from torchvision import datasets,transforms,models
import matplotlib.pyplot as plt 
import time
import os
import copy
from PIL import Image,ImageOps
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
plt.ion()  # interactive mode

# Data augmentation and normalization for training
# Just normalization for validation
data_transforms ={
	'train':transforms.Compose([
		transforms.Resize((224,224)),
		transforms.RandomHorizontalFlip(),
		transforms.ToTensor(),
		transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
		]),
	'val':transforms.Compose([
		transforms.Resize((224,224)),
		transforms.ToTensor(),
		transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
		]),
}

data_dir='training_image_data'
image_datasets={x:datasets.ImageFolder(os.path.join(data_dir,x),data_transforms[x])
				for x in ['train','val']}
dataloaders={x:torch.utils.data.DataLoader(image_datasets[x],batch_size=4,shuffle=True,num_workers=1)
				for x in ['train','val']}
dataset_sizes={x:len(image_datasets[x]) for x in ['train','val']}
class_names=image_datasets['train'].classes 
device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def imshow(inp,title=None):
	inp=inp.numpy().transpose((1,2,0))
	mean=np.array([0.485,0.456,0.406])
	std=np.array([0.229,0.224,0.225])
	inp=std*inp+mean
	inp=np.clip(inp,0,1)
	plt.imshow(inp)
	if title is not None:
		plt.title(title)
	plt.pause(5) # pause a bit so that plots are updated

# Get a batch of training data
#inputs,classes=next(iter(dataloaders['train']))

# Make a grid from batch
# out=torchvision.utils.make_grid(inputs)

# imshow(out,title=[class_names[x] for x in classes])

def train_model(model,criterion,optimizer,scheduler,num_epochs):
		since=time.time()

		best_model_wts=copy.deepcopy(model.state_dict())
		best_acc=0.0

		for epoch in range(num_epochs):
			print('Epoch {}/{}'.format(epoch,num_epochs-1))
			print('-'*10)	

			# Each epoch has a training and validation phase
			for phase in ['train','val']:
				if phase == 'train':
					model.train()  # Set model to training mode
				else:
					model.eval()  # Set model to evaluate mode

				running_loss=0.0
				running_corrects=0

				# Iterate over data.
				for inputs,labels in dataloaders[phase]:
					inputs=inputs.to(device)
					labels=labels.to(device)
					
					# zero the parameter gradients
					optimizer.zero_grad()

					# forward
                	# track history if only in train
					with torch.set_grad_enabled(phase =='train'):
						outputs=model(inputs)
						_,preds=torch.max(outputs,1)
						loss=criterion(outputs,labels)

						# backward + optimize only if in training phase
						if phase == 'train':
							loss.backward()
							optimizer.step()

					# statistics
					running_loss+=loss.item()*inputs.size(0)
					running_corrects+=torch.sum(preds==labels.data)
				if phase=='train':
					scheduler.step()  #learning rate

				epoch_loss = running_loss/dataset_sizes[phase]
				epoch_acc=running_corrects.double()/dataset_sizes[phase]

				print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase,epoch_loss,epoch_acc))

				# deep copy the model
				if phase== 'val' and epoch_acc > best_acc:
					best_acc=epoch_acc
					best_model_wts=copy.deepcopy(model.state_dict())

				print()

		time_elapsed = time.time() - since
		print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed/60,time_elapsed%60))
		print('Best val Acc: {:4f}'.format(best_acc))

		# load best model weights
		model.load_state_dict(best_model_wts)
		return model

#set test dataset to transform
class PDF_DataSet(torch.utils.data.Dataset):
	def __init__(self,image_list,transform=None):
		self.image_list=image_list
		self.transform=transform
	def __len__(self):
		return len(self.image_list)
	def __getitem__(self,idx):
		if torch.is_tensor(idx):
			idx=idx.tolist()
		sample=self.image_list[idx]
		if self.transform:
			sample=self.transform(sample)
		return [sample.float(),1]         #1 is unsigned label 



#divide each images in the list into four small images
def splitUp_image(imageList):     
	new_list=[]
	for i in imageList:
		Invert_i=ImageOps.invert(i)
		i=i.crop(Invert_i.getbbox())
		width,height=i.size
		new_list.append(i.crop((0,0,width//2+50,height//2+50)))
		new_list.append(i.crop((width//2-50,0,width,height//2+50)))
		new_list.append(i.crop((0,height//2-50,width//2+50,height)))
		new_list.append(i.crop((width//2-50,height//2-50,width,height)))

	return new_list


# Second judgment on the result
# If you ignore this function, it does not affect the program operation -- future inprovement
# This function works on the Linux system, it can improve 3% acc. But it fails on the Windows system. The problem may be related to obsolete "transform" torchvision function due to version diff.
def doublecheck(model,image,standard):
	print('doublecheck')
	print(image.size()) 
	aug_list=[]
	aug_list.append(transforms.RandomHorizontalFlip(1).forward(image))
	aug_list.append(transforms.RandomVerticalFlip(1).forward(image))
	aug_list.append(transforms.RandomRotation((0,10)).forward(image))
	aug_list.append(transforms.RandomRotation((10,100)).forward(image))
	aug_list.append(transforms.RandomRotation((100,200)).forward(image))
	aug_list.append(transforms.RandomRotation((200,300)).forward(image))
	aug_list.append(transforms.RandomRotation((300,360)).forward(image))
	signed=0
	for i in aug_list:
		outputs=model(i)
		_,preds=torch.max(outputs,1)
		if(preds.item()==0):
			signed+=1
	if(signed>=standard):
		return 1
	return 0

#predic the pdf file by a image list
def test_imgList(model,images):  
	was_training=model.training
	model.eval()
	
	new_images=splitUp_image(images)

	with torch.no_grad():
		data_transforms = transforms.Compose([       
			transforms.Resize((224,224)),
    		transforms.ToTensor(),
    		transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    	])

		dataset_pdf=PDF_DataSet(new_images,data_transforms)                  
		pdf_data=torch.utils.data.DataLoader(dataset_pdf,batch_size=1,num_workers=0)

		for i,(pdf_input,pdf_label) in enumerate(pdf_data):
			outputs=model(pdf_input)
			_,preds=torch.max(outputs,1)

			if preds.item()==0:
				return 1

			# running doublecheck function. Uncomment the block below and comment the two lines of code above
			##########
			# if preds.item()==0:
			# 	print(preds.item())
			# 	if(doublecheck(model,pdf_input,1)==1):
			# 		# print("yep")
			# 		return 1
			# 	else:
			# 		print('blocked')
			# else:
			# 	if((doublecheck(model,pdf_input,2)==1 and i>=len(pdf_data)-8)):
			# 		print('saved')
			# 		return 1
			##########

	model.train(mode=was_training)		
	return 0

#data processing, classification result by trained module and stastic the test accuracy
def pdf_validation(model):
	# test data (pdf files) processing
	dir1="test_pdf_data/signed"
	dir0="test_pdf_data/unsigned"
	signed_pdf = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]
	unsigned_pdf = [f for f in os.listdir(dir0) if os.path.isfile(os.path.join(dir0, f))]

	correct=0
	total=len(signed_pdf)+len(unsigned_pdf)
	signed_count=0
	unsigned_count=0

	for f in signed_pdf:
		# transfore a pdf file to a image list
		images=convert_from_path(os.path.join(dir1, f))
		print("Processing signed:{}/{}".format(signed_count,len(signed_pdf)))
		signed_count+=1
		if(test_imgList(model,images)==1):
			correct+=1
		else:
			print(f)

	for f in unsigned_pdf:
		images=convert_from_path(os.path.join(dir0, f))
		print("Processing unsigned:{}/{}".format(unsigned_count,len(unsigned_pdf)))
		unsigned_count+=1
		if(test_imgList(model,images)==0):
			correct+=1
		else:
			print(f)
	print("total accuracy is: ",correct/total)

	return


#Uncomment the block below to train model 
##########
# model_ft=models.resnet50(pretrained=True)
# num_ftrs=model_ft.fc.in_features
# # Here the size of each output sample is set to 2.
# model_ft.fc=nn.Linear(num_ftrs,2)

# model_ft=model_ft.to(device)

# criterion=nn.CrossEntropyLoss()

# # Observe that all parameters are being optimized
# optimizer_ft=optim.SGD(model_ft.parameters(),lr=0.001,momentum=0.9)

# # Decay LR by a factor of 0.1 every 7 epochs
# exp_lr_scheduler=lr_scheduler.StepLR(optimizer_ft,step_size=7,gamma=0.1)

# model_ft=train_model(model_ft,criterion,optimizer_ft,exp_lr_scheduler,num_epochs=20)

# # if training new model, please rename to avoid cover
# torch.save(model_ft,"trained_model_resnet50")
##########

model_ft=torch.load("trained_model_resnet50")

#pdf testing 
pdf_validation(model_ft)