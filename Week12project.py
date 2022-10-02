#!/user/bin/env python3.8

# Week 12:Create a list of AWS Services 

# objectives
# Create a list of Services IE S3, Lambda, EC2, etc.
# 1. The list should be empty intially. 
# 2. Populate the list using append or insert.
# 3. Print the list and the length of the list.
# 4. Remove two specific services from the list by name or by index.
# 5. Print the new list and the length of the list 

# Objective 1 - Create an empty list
services = []

# Objective 2 - Populate the list using append or insert 
services.append("DynamoDB")
services.append("S3")
services.append("mySQL")
services.append("Cloudwatch")
services.append("codepipeline")

# Objective 3 - Print the list and the length of the list 
print(services)

# Objective 4 - Remove two specific services from the list by name or by index
services.remove("Cloudwatch")
services.remove("codepipeline")
print(services)

# Objective 5 - Print the new list and the new length of the list 
print(len(services))