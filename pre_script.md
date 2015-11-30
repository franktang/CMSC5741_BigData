Thanks Vivien.  

Noramly, when you shop online, there are millions of products, inbetween you can find some of them are quite similar.
However, how can a system identify it. One way is to identify the terms similarity.

For a product, its title contains many information, style, brand or others.   
Take below two skirts as an example. We can find the two products' title have XXXXXXXXXX in common. We can say to some extend,
they are common. Also, they have distinct characteristic, say for example, the left one is house print, while the right one is
the cartoon print.

Here we have a dataset, which contains the item id, category id, terms (pls be noted that the terms has already been transformed
into numbers), and image data (it's optional, not all items has, today we may focus on the terms)   
Here are some sample data.

Firslty, we will create a boolean matrix item by item, where rows are for terms and cols are for items. 

Then, we will perform MinHash and LSH on the boolean matrix in our first step. Let's recap here, the signature matrix M is divided into b bands, and for each band, we perform LSH, the cols whose hash value falls into the same bucket is regarded as a candidate pair.   
In our program, we take band size = 10 and bucket size = 10. and here are the LSH result.

The final step is to measure the two items similarity.    
For each item in the test item list, calculate the jaccard similarity with items in the same category

For example, for the test item 2523677, here are the lsh hash values lists which are in the same category as this one.
For item 2248318, we can find 60% of bands are identical in lsh hash values, we output similarity 0.6 here.
For item 717223, since at every band, their lsh hash value are the same, we output similarity 1.0 here.
