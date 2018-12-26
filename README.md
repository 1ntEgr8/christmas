# What does this tool do?

This tool provides you with an easy way to send UNIQUE christmas greetings! It generates a pixelated Christmas Tree greeting and provides users with a shareable link, which recepients can then claim from Santa. The best part about this is that each 
greeting is UNIQUE and is based on a seed value assigned to you. Your greeting cannot get more personal than that!

# How do I use this tool?

First, you need to place an order to Santa. All Santa needs is your name, email, and a recepient list. After having placed an order, Santa will provide you with a link which you can then send to your recepients. Recepients can then access your check-in link. They only have to enter their first name to retrieve their gift. It really is that simple!

# How does the program make the tree?

I have programmed a Tree Creation algorithm. There a couple of things that happen in the background to ensure that your greeting card is unique. Once an order is placed, a seed value matrix (which is a list of numbers that map to color combinations for the tree) is created. This is used to generate the greeting for your first recepient. Then this matrix is multiplied by a stochastic matrix to get a new matrix (which is, again, a list of numbers that map to color combinations for the tree). This is then used to create the next tree.

## Obtain the Seed Value Matrix
### What is the Seed Value Matrix?
This is a 20x20 lower triangular matrix whose values are keys to a color dictionary which contains all of the green shades used in the making of the tree
### How do you make it?
The Seed Value matrix is made randomly using the random function of python
### What do you do with it?
This Seed Value matrix is then processed to add bobtails onto the tree, thereby creating a new matrix. This matrix is then used to plot the pixels on the canvas. After adding a couple of finishing touches, your first card is ready!

## Multiply by thematrix
### What is thematrix?
thematrix is a 20x20 stochastix matrix. The modified Seed Value Matrix is multiplied by thematrix to obtain a new 20x20 matrix. You can check out it's values in this repo.
### What do you do with this new 20x20 matrix?
This new matrix is further processed to ensure only values that map to shades of green exist. Then it is processed to add bobtails.
### Why do you need thematrix?
thematrix makes it easier for 1ntEgr8 to hash your unique tree color combinations. Further, multiplying by this matrix improves the chances of getting a totally random matrix. Also, it makes sure that all of your greetings stem from your Seed Value Matrix, thereby adding an added level of uniqueness to your card.

## Make the greeting, then repeat
### What next?
This process is continued. All of the matrix data is stored onto a json file.
### How do you process requests?
A python script is run that checks the database for new requests. It then processes those requests in batches. This helps prevent unecessary lag in content delivery.


**YOU CAN SEE SAMPLES IN THE REPO. THEY EXIST IN surprise/static folder**
