#for loop training
text =["set one", "set two", "set three", "set four"]
text2 =["specific one","specific two","specific three","specific four"]

# check for blank tuple arrays before for loop
if text or text2:
    print("must have a set and specific to proceed")
    exit 

# nested loop through the two arrays
for x in text:
    for y in text2:
         if x == "set one":
             print("set one not allowed")
             break
         else:
             if y == "specific one":
                 print("specific one not allowed")
             else:
                 print(x,y)