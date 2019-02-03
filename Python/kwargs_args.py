"""
# Small demo on using *args and **kwargs in Python
# Was earlier used in ImageDataBunch

# Let's look at the source code of it.

from_df(path: PathOrStr, df: DataFrame, folder: PathOrStr=None, \
        label_delim: str=None, valid_pct: float=0.2, fn_col: IntsOrStrs=0, \
        label_col: IntsOrStrs=1, suffix: str='', **kwargs: Any) -> ImageDataBunch

# Usage
df = pd.read_csv(path/"labels.csv", header='infer')
df.head()

data = ImageDataBunch.from_df(path, df, ds_tfms=tfms, size=24)

# what is the use of size
# used in create_from_ll
def create_from_ll(cls, lls:LabelLists, bs:int=64, df_tfms:Optional, \
        num_workers:int=defaults.cpus, dl_tfms:Optional, test:Optional, \
        collate_fn:Callable=data_collate, **kwargs)->'ImageDataBunch'
# creates an `ImageDataBunch` from `LabelLists` `lls` with potential `ds_tfms`
lls = lls.transform(tfms=df_tfms, size=size, **kwargs)
"""

def myFun(*argv):
    for arg in argv:
        print(arg, end=' ')
    print("\n")

# doesn't necessarily have to be *argv, *args or anything
# can be like *kush as well.
def new_fun(*kush):
    for arg in kush:
        print(arg, end= ' ')
    print("\n")

# what about **kwargs?
def kwargs_use(**kwargs):
    # keyworder variable length arguments
    # like: kwargs_use(slide=2, size=27)
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

myFun('kushashwa', 'ravi', 'shrimali')
new_fun("kushashwa", "ravi", "shrimali")
kwargs_use(first_name="Kushashwa", mid_name="Ravi", last_name="Shrimali")

