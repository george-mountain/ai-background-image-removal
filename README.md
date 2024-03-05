### AI Background Image Removal

Remove background from any images using AI



# gettin started

Clone this repo:

git clone https://github.com/george-mountain/ai-background-image-removal.git


### AI model download
Download the model by cloning its repo:

git clone https://huggingface.co/briaai/RMBG-1.4

Copy the model.pth file from RMBG-1.4 to the backend folder

## Running the application

use the Makefile commands to run the apps
 1. build the docker images:

 ```
    make build
```

2. run the docker containers

```
    make up-v
```