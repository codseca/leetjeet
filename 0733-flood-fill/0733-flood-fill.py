from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]

        # If starting color is already the same as new color
        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        queue = deque()
        queue.append((sr, sc))

        image[sr][sc] = color  # mark visited by coloring

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    image[nr][nc] == original):

                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image
