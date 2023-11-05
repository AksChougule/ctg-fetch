========
fetchctg 
========

Python functions to fetch formatted safety data from the clinicaltrials.gov API.


* Free software: MIT license


## Tutorial
--------


### How to install

```sh
$ pip install fetchctg
```

### Basic Usage

```sh
import ctgfetch as ctf
	
# Get serious adverse events from trial id NCT01859988
df = get_sae("NCT01859988")

# Save non-serious adverse events to excel file in local directory
save_oae("NCT01859988")

# Get non-serious adverse events from trial id NCT01859988
df = get_oae("NCT01859988")

# Save serious adverse events to excel file in local directory
save_sae("NCT01859988")

# Get all (serious and non-serious) adverse events from trial id NCT01859988
df = get_all_ae("NCT01859988")

# Save all (serious and non-serious) adverse events to excel file in local directory
save_all_ae("NCT01859988")
```
