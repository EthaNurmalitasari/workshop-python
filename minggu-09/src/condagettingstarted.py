# Managing environments
# Create a new environment and install a package in it
conda create --name snowflakes biopython

Proceed ([y]/n)? y
# Type "y" and press Enter to proceed.

# To use, or "activate" the new environment, type the following:
-conda activate only works on conda 4.6 and later versions.

# Io see a list of all your environments, type:
conda info --envs

# A list of environments appears, similar to the following:
conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes

Change your current environment back to the default (base): conda activate
For versions prior to conda 4.6, use:

Windows: activate

macOS, Linux: source activate


# Managing Python
3 Create a new environment named "snakes" that contains Python 3.9:
conda create --name snakes python=3.9

# Activate the new environment:
Windows: conda activate snakes
macOS and Linux: conda activate snakes

# Verify that the snakes environment has been added and is active:
conda info --envs

# Conda displays the list of all environments with an asterisk (*) after the name of the active environment:
# conda environments:
#
base                     /home/username/anaconda3
snakes                *  /home/username/anaconda3/envs/snakes
snowflakes               /home/username/anaconda3/envs/snowflakes

# The active environment is also displayed in front of your prompt in (parentheses) or [brackets] like this:
(snakes) $

# Verify which version of Python is in your current environment:
python --version

# Deactivate the snakes environment and return to base environment: conda activate

# Managing packages
conda search beautifulsoup4
conda install beautifulsoup4
conda list