# Create Jar
1. Compile HelloWorld.java
```
javac HelloWorld.java 
```

2. Create jar
```
jar cfe hello_world.jar HelloWorld HelloWorld.class
```
c ... create new jar/archive 
f ... set filename (hello_world.jar)
e ... entrypoint (HelloWorld)
HelloWorld.class ... file inside jar/archive

# Run
```
java -jar hello_world.jar 
```
