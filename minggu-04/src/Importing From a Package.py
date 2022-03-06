# This would mean that from sound.effects import * would import the three named submodules of the sound package
__all__ = ["echo", "surround", "reverse"]

# It also includes any submodules of the package that were explicitly loaded by previous import statements
import sound.effects.echo
import sound.effects.surround
from sound.effects import *