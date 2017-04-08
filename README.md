# flask_sample
##Understand how to use flask in a simple way 
##Steps:
1.    create a file chamado body.json
2.    with this content {"color":"orange"}
3.    send it to the api in this way : curl -H "Content-Type: application/json" -X POST -d@body.json localhost:5000/transform/1
4.    get it back in this way : curl localhost:5000/transform/1
##You can change the number at the end of the post
##Thank you, [Gleicon](https://github.com/gleicon)
