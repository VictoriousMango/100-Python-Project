import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import os
import cv2
load_dotenv()
testFile = os.getenv('testFile').replace("var", "test.png")
iterations = []
for limit in range(1, 6):
    arr = np.random.randint(0, 255, (limit, limit), dtype=np.uint8)
    iterator = 0
    for i in range((limit * limit)):
        for j in range(limit * limit -2):
            iterator += 1
            arr[j//limit][j%limit], arr[(j//limit)][(j%limit)+1] = min(arr[j//limit][j%limit], arr[(j//limit)][(j%limit)+1]), max(arr[j//limit][j%limit], arr[(j//limit)][(j%limit)+1])
            plt.title(f"Iteration: {iterator} - Swapping Indexes {i} and {j}")
            plt.imshow(arr, cmap='hot')
            plt.colorbar()
            plt.scatter(i%limit, i//limit, color='red', marker='X')
            plt.scatter(j%limit, j//limit, color='black', marker='X')
            plt.savefig(testFile)
            plt.close()
            cv2.imshow("Random Image", cv2.imread(testFile))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    iterations.append(iterator)
    plt.plot(range(1, len(iterations)+1), iterations, marker='o')
    plt.title("Number of Iterations vs Array Size")
    plt.xlabel("Array Size (n x n)")
    plt.ylabel("Number of Iterations")
    plt.savefig(testFile)
    plt.close()
    cv2.imshow("Iterations Plot", cv2.imread(testFile))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break