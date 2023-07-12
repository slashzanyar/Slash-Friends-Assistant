# Importing General Modules 
import random

# Add Extensions
import messages

# Add Variables
sm = messages.start_messages
rsm = messages.restart_messages
dm = messages.damage_messages
adm = messages.add_damage_messages
nfm = messages.no_fosh_messages

# Randomize Messages
    # Randomize: start command masseges
def MR_start(sm):
    return random.choice(sm)

    # Randomize: restart command messages
def MR_restart(rms):
    return random.choice(rsm)

    # Randomize: add damage command
def MR_add_damage(adm):
    return random.choice(adm)
    
    # Randomize: damage messages
def MR_damage(dm):
    return random.choice(dm)

    # Randomize: no fosh messages
def MR_no_fosh(nfm):
    return random.choice(nfm)
