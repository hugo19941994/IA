FROM openjdk:11.0.2

# Install dependencies
RUN apt-get update
RUN apt-get install -y maven python3 python3-pip less

# Install parser dependencies
ADD parser /parser
RUN python3 -m pip install -r /parser/requirements.txt

WORKDIR /code
# Prepare by downloading dependencies
ADD backend/pom.xml /code/pom.xml

RUN mvn dependency:resolve
RUN mvn verify

# Adding source, compile and package into a fat jar
ADD backend/src /code/src


RUN mvn package

EXPOSE 8080
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar", "target/cv-parser-1.0.0.jar"]
