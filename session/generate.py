from virp import Session
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    # Default Settings
    Session()

    # Custom Settings (for testing)
    #Session(folder_path = "_disordered_cifs", mindist = 10, sample_size = 2)