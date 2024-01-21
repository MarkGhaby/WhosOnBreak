import cv2
import numpy as np
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        # Process the file here
      class TimeBlock:
        day = 0
        start = 0
        end = 0
        def __init__(self, day, start, end):
          self.day = day
          self.start = start
          self.end = end
        def toString(self):
          string = "day: ", self.day, " from: ", self.start, " to: ", self.end
          return string
        def sharedAvailability(self, otherTimeBlock):
          if self.day != otherTimeBlock.day:
            return None
          S1 = self.start
          S2 = otherTimeBlock.start
          E1 = self.end
          E2 = otherTimeBlock.end
          largestStart = None
          smallestEnd = None
          if S1 > S2:
            largestStart = S1
          else:
            largestStart = S2
          if E1 < E2:
            smallestEnd = E1
          else:
            smallestEnd = E2
          if (E2 > S1 and S2 < E1):
            time = TimeBlock(self.day, largestStart, smallestEnd)
            return time
          elif (E1 > S2 and S1 < E2):
            time = TimeBlock(self.day, largestStart, smallestEnd)
            return time
          else:
            return None

      leftMargin = 68
      hourHeight = 170
      columnWidth = 160
      quaterHeight = 43

      def show(image):
        cv2.imshow("image", image)
        cv2.waitKey(0)

      def showScaled(image, ratio):
        scale_factor = ratio
        newWidth = int(image.shape[1] * scale_factor)
        newHeight = int(image.shape[0] * scale_factor)
        scaledImage = cv2.resize(image, (newWidth, newHeight))
        show(scaledImage)

      def cropImageVertically(image):
        pixelsToCrop = findLightGrayPixelVertical(image)
        y1 = 0 + pixelsToCrop
        y2 = image.shape[0]
        return image[y1:y2, 0:image.shape[1]]

      def cropImageHorizontally(image):
          x1 = leftMargin
          x2 = image.shape[1]
          return image[0:image.shape[0], x1:x2]

      def findLightGrayPixelVertical(image):
        grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lightGrayThreshold = 200
        for y in range(grayImage.shape[0]):
            pixelValue = grayImage[y, 4]
            if pixelValue >= lightGrayThreshold:
                return y
        return 0

      def isGreen(pixel, green_threshold=50):
        b, g, r = pixel
        return g > max(r, b) + green_threshold

      #vertical iteration (finding edges)
      def findVerticalGreenEdges(image, column):
        edges = []
        lowestEdge = image.shape[0]
        for row in range(5, image.shape[0] - 6, 5):
          if ((isGreen(image[row, column]) and not isGreen(image[row + 5, column])) or (not isGreen(image[row, column]) and isGreen(image[row + 5, column]))):
            edges.append(row+2)
        return edges

      #horizontal iteration
      def getClassTimes(image, startTime):
        edges = []
        times = []
        for i in range(15, 800, 159):
          edges.append(findVerticalGreenEdges(image, i))
        lowestEdge = image.shape[0]
        for edge in edges:
          for singleEdge in edge:
            if singleEdge < lowestEdge:
              lowestEdge = singleEdge
        for i in range(len(edges)):
          for j in range(len(edges[i])):
            edges[i][j] -= lowestEdge
        for i in range(len(edges)):
          if len(edges[i]) != 0:
            for j in range(0, len(edges[i]), 2):
              startInMinutes = round((((edges[i][j])/40) * 15)/15)*15
              endInMinutes = round((((edges[i][j+1])/40) * 15)/15)*15
              times.append(TimeBlock(i, startInMinutes + startTime, endInMinutes + startTime))
        return times



      #[vertical][horizontal]
      def getData(name, startTime):
        image = cv2.imread(name)
        image = cropImageVertically(image)
        image = cropImageHorizontally(image)
        classTimes = getClassTimes(image, startTime)
        return classTimes

      return 'File successfully processed', 200

if __name__ == '__main__':
    app.run(debug=True)

