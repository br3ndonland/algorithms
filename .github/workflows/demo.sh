#! /bin/sh

echo "Hello World, from an external shell script!"
if [ "$BUILD_ENV" = "demo" ]; then
  echo "This is a demo."
elif [ "$BUILD_ENV" ]; then
  echo "BUILD_ENV=$BUILD_ENV"
else
  echo "There isn't a BUILD_ENV variable set."
fi
if [ "$SPAM_STRING" ]; then echo "Did you know that $SPAM_STRING?"; fi
