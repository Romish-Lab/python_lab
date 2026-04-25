# 5. Modify above function so that it has default values of 2 for both length and width.
def rect_def(l=2, w=2):
    area = l * w
    peri = 2 * (l + w)
    return area, peri

print(rect_def())           
print(rect_def(5, 3))      
