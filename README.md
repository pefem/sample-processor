# sample-processor
The Sample processor takes a given image and based on a predefined set of parameters yields a set of randomly selected sections of an origin image.

# How to Run
To this code simply install pipenv and run the command "pipenv install" to install required dependencies. This is the recomended method as it would give a deterministic versions 
of the dependencies used. Alternatively a requirements.txt file has also been provided.

# Structure
The Code structure is comprised of 3 main files/modules: 'sample_interface', 'image_sample' and 'app.py'. Please see description of files and folders below

  # sample_interface: contains an abstract class which serves as a template from which other samples types can be defined
  # Image_sample: contains class which inherits from 'sample_interface'. Primary focus of this class is on Image sampling
  # app.py: entry point to program
  # random_samples: folder which holds generated samples
  # images: folder for origin image, currently holds a default image 'buildings.jfif'
  # logs: contains log files
