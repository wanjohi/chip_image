## Prerequisites

- OpenCV
- Docker
- Django
- numpy

## Note
- No effort was put into making this clean and efficient. The code and implementation will need
to be improved.
- Basic tests have been done on this system, no error handling or effort into a pretty
interface
-There are redundant libaries included in this image, they need to be cleaned up later on

## Lessons
- You need to specify an ARM image for docker-compose
- Images uploaded need to be translated into a 2d numpy array, then opencv, then back to 3d numpy array

## Issues
- Unable to build a docker with scikit-image. This resulted in a big change to the code
design, or basic image comparison is done.
- Django files are created in the wrong folders, they needed to be moved around after creating the
docker image.

## Credit
http://www.pyimagesearch.com/2014/09/15/python-compare-two-images/
