#!/bin/bash

# List of images to push
images=(
  "myrepo/image1:tag1"
  "myrepo/image2:tag2"
  "myrepo/image3:tag3"
)

# Push each image in the background
for image in "${images[@]}"; do
  docker push "$image" &
done

# Wait for all background processes to finish
wait

echo "All images have been pushed."