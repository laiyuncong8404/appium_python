# ========================================================
# Summary        :myExceotion
# Author         :tong shan
# Create Date    :2015-09-28
# Amend History  :
# Amended by     :
# ========================================================

class myError(Exception):

    def __init__(self, value):
        self.value = value


