'''
How to Create the requirement.txt for FastAPI on Heroku
Heroku requires the requirement.txt to install your Python packages. pipreqs [6] generates it based on imports in your project.
'''
'''
pip install pipreqs
cd my_new_project
pipreqs ./
# if you already have the requirement.txt
 pipreqs --force ./
'''
 
'''
Since pipreqs generates it based on import, you need to add the following to the requirements.txt manually.
'''