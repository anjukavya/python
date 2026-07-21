# 1.	Solid Square Pattern
# Problem: Print a solid square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *
n=3
for i in range(1,n+1):
    stars=""
    for j in range(1,n+1):
        stars+="* "
    print(stars)


# 2.	Solid Rectangle Pattern
# Problem: Print a solid rectangle of m rows and n columns.
# Input: m = 3
# Output:
# * * * * * *
# * * * * * *
# * * * * * *
n=3
for i in range(1,n+1):
    stars=""
    for j in range(1,n*2+1):
        stars+="* "
    print(stars)

# 3.	Right-Angled Triangle (Left-Aligned)
# Problem: Print a left-aligned right-angled triangle.
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
n=4
for i in range(1,n+1):
    stars=""
    for j in range(1,i+1):
        stars+="* "
    print(stars)

#    * 
#   * * 
#  * * * 
# * * * * 
n=4
for i in range(1,n+1):
    space=""
    for k in range(n-i,0,-1):
       space+=" "
    stars=""
    for j in range(1,i+1):
       stars+="* "
    print(space+stars)

# 4.	Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
n=5
for i in range(1,n+1):
    spaces=""
    for j in range(n-i,0,-1):
        spaces+="  "
    stars=""
    for k in range(1,i+1):
        stars+="* "
    print(spaces+stars)


# 5.	Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for i in range(n,0,-1):
    stars=""
    for j in range(1,i+1):
        stars+="* "
    print(stars)

# 6.	Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
n=5
for i in range(n,0,-1):
    spaces=""
    for j in range(0,n-i):
        spaces+="  "
    stars=""
    for k in range(1,i+1):
        stars+="* "
    print(spaces+stars)

# 7.	Centered Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     * * *
#   * * * * *
# * * * * * * *
n=4
for i in range(1,n+1):
    spaces=""
    for j in range(n-i):
        spaces+="  "
    stars=""
    for k in range(1,i+i):
        stars+="* "
    print(spaces+stars)


# 8.	Diamond Pattern
# Input: n = 3
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *
n=3
for i in range(1,n+1):
    spaces=""
    for j in range(n-i):
        spaces+="  "
    stars=""
    for k in range(1,i+i):
        stars+="* "
    print(spaces+stars)
for i in range(n-1,0,-1):
    spaces=""
    for j in range(n-i):
        spaces+="  "
    stars=""
    for k in range(1,i+i):
        stars+="* "
    print(spaces+stars)









