

**PROBLEM** : Use the house price prediction dataset available in https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data. Perform feature engineering, Random Forest, and gradient boosting and predict sales prices.

DATA DESCRIPTION

MSSubClass: Identifies the type of dwelling involved in the sale.

        20	1-STORY 1946 & NEWER ALL STYLES
        30	1-STORY 1945 & OLDER
        40	1-STORY W/FINISHED ATTIC ALL AGES
        45	1-1/2 STORY - UNFINISHED ALL AGES
        50	1-1/2 STORY FINISHED ALL AGES
        60	2-STORY 1946 & NEWER
        70	2-STORY 1945 & OLDER
        75	2-1/2 STORY ALL AGES
        80	SPLIT OR MULTI-LEVEL
        85	SPLIT FOYER
        90	DUPLEX - ALL STYLES AND AGES
       120	1-STORY PUD (Planned Unit Development) - 1946 & NEWER
       150	1-1/2 STORY PUD - ALL AGES
       160	2-STORY PUD - 1946 & NEWER
       180	PUD - MULTILEVEL - INCL SPLIT LEV/FOYER
       190	2 FAMILY CONVERSION - ALL STYLES AND AGES

MSZoning: Identifies the general zoning classification of the sale.

       A	Agriculture
       C	Commercial
       FV	Floating Village Residential
       I	Industrial
       RH	Residential High Density
       RL	Residential Low Density
       RP	Residential Low Density Park
       RM	Residential Medium Density

LotFrontage: Linear feet of street connected to property

LotArea: Lot size in square feet

Street: Type of road access to property

       Grvl	Gravel
       Pave	Paved

Alley: Type of alley access to property

       Grvl	Gravel
       Pave	Paved
       NA 	No alley access

LotShape: General shape of property

       Reg	Regular
       IR1	Slightly irregular
       IR2	Moderately Irregular
       IR3	Irregular
       
LandContour: Flatness of the property

       Lvl	Near Flat/Level
       Bnk	Banked - Quick and significant rise from street grade to building
       HLS	Hillside - Significant slope from side to side
       Low	Depression

Utilities: Type of utilities available

       AllPub	All public Utilities (E,G,W,& S)
       NoSewr	Electricity, Gas, and Water (Septic Tank)
       NoSeWa	Electricity and Gas Only
       ELO	Electricity only

LotConfig: Lot configuration

       Inside	Inside lot
       Corner	Corner lot
       CulDSac	Cul-de-sac
       FR2	Frontage on 2 sides of property
       FR3	Frontage on 3 sides of property

LandSlope: Slope of property

       Gtl	Gentle slope
       Mod	Moderate Slope
       Sev	Severe Slope

Neighborhood: Physical locations within Ames city limits

       Blmngtn	Bloomington Heights
       Blueste	Bluestem
       BrDale	Briardale
       BrkSide	Brookside
       ClearCr	Clear Creek
       CollgCr	College Creek
       Crawfor	Crawford
       Edwards	Edwards
       Gilbert	Gilbert
       IDOTRR	Iowa DOT and Rail Road
       MeadowV	Meadow Village
       Mitchel	Mitchell
       Names	North Ames
       NoRidge	Northridge
       NPkVill	Northpark Villa
       NridgHt	Northridge Heights
       NWAmes	Northwest Ames
       OldTown	Old Town
       SWISU	South & West of Iowa State University
       Sawyer	Sawyer
       SawyerW	Sawyer West
       Somerst	Somerset
       StoneBr	Stone Brook
       Timber	Timberland
       Veenker	Veenker

Condition1: Proximity to various conditions

       Artery	Adjacent to arterial street
       Feedr	Adjacent to feeder street
       Norm	Normal
       RRNn	Within 200' of North-South Railroad
       RRAn	Adjacent to North-South Railroad
       PosN	Near positive off-site feature--park, greenbelt, etc.
       PosA	Adjacent to postive off-site feature
       RRNe	Within 200' of East-West Railroad
       RRAe	Adjacent to East-West Railroad

Condition2: Proximity to various conditions (if more than one is present)

       Artery	Adjacent to arterial street
       Feedr	Adjacent to feeder street
       Norm	Normal
       RRNn	Within 200' of North-South Railroad
       RRAn	Adjacent to North-South Railroad
       PosN	Near positive off-site feature--park, greenbelt, etc.
       PosA	Adjacent to postive off-site feature
       RRNe	Within 200' of East-West Railroad
       RRAe	Adjacent to East-West Railroad

BldgType: Type of dwelling

       1Fam	Single-family Detached
       2FmCon	Two-family Conversion; originally built as one-family dwelling
       Duplx	Duplex
       TwnhsE	Townhouse End Unit
       TwnhsI	Townhouse Inside Unit

HouseStyle: Style of dwelling

       1Story	One story
       1.5Fin	One and one-half story: 2nd level finished
       1.5Unf	One and one-half story: 2nd level unfinished
       2Story	Two story
       2.5Fin	Two and one-half story: 2nd level finished
       2.5Unf	Two and one-half story: 2nd level unfinished
       SFoyer	Split Foyer
       SLvl	Split Level

OverallQual: Rates the overall material and finish of the house

       10	Very Excellent
       9	Excellent
       8	Very Good
       7	Good
       6	Above Average
       5	Average
       4	Below Average
       3	Fair
       2	Poor
       1	Very Poor

OverallCond: Rates the overall condition of the house

       10	Very Excellent
       9	Excellent
       8	Very Good
       7	Good
       6	Above Average
       5	Average
       4	Below Average
       3	Fair
       2	Poor
       1	Very Poor

YearBuilt: Original construction date

YearRemodAdd: Remodel date (same as construction date if no remodeling or additions)

RoofStyle: Type of roof

       Flat	Flat
       Gable	Gable
       Gambrel	Gabrel (Barn)
       Hip	Hip
       Mansard	Mansard
       Shed	Shed

RoofMatl: Roof material

       ClyTile	Clay or Tile
       CompShg	Standard (Composite) Shingle
       Membran	Membrane
       Metal	Metal
       Roll	Roll
       Tar&Grv	Gravel & Tar
       WdShake	Wood Shakes
       WdShngl	Wood Shingles

Exterior1st: Exterior covering on house

       AsbShng	Asbestos Shingles
       AsphShn	Asphalt Shingles
       BrkComm	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       CemntBd	Cement Board
       HdBoard	Hard Board
       ImStucc	Imitation Stucco
       MetalSd	Metal Siding
       Other	Other
       Plywood	Plywood
       PreCast	PreCast
       Stone	Stone
       Stucco	Stucco
       VinylSd	Vinyl Siding
       Wd Sdng	Wood Siding
       WdShing	Wood Shingles

Exterior2nd: Exterior covering on house (if more than one material)

       AsbShng	Asbestos Shingles
       AsphShn	Asphalt Shingles
       BrkComm	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       CemntBd	Cement Board
       HdBoard	Hard Board
       ImStucc	Imitation Stucco
       MetalSd	Metal Siding
       Other	Other
       Plywood	Plywood
       PreCast	PreCast
       Stone	Stone
       Stucco	Stucco
       VinylSd	Vinyl Siding
       Wd Sdng	Wood Siding
       WdShing	Wood Shingles

MasVnrType: Masonry veneer type

       BrkCmn	Brick Common
       BrkFace	Brick Face
       CBlock	Cinder Block
       None	None
       Stone	Stone

MasVnrArea: Masonry veneer area in square feet

ExterQual: Evaluates the quality of the material on the exterior

       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor

ExterCond: Evaluates the present condition of the material on the exterior

       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor

Foundation: Type of foundation

       BrkTil	Brick & Tile
       CBlock	Cinder Block
       PConc	Poured Contrete
       Slab	Slab
       Stone	Stone
       Wood	Wood

BsmtQual: Evaluates the height of the basement

       Ex	Excellent (100+ inches)
       Gd	Good (90-99 inches)
       TA	Typical (80-89 inches)
       Fa	Fair (70-79 inches)
       Po	Poor (<70 inches
       NA	No Basement

BsmtCond: Evaluates the general condition of the basement

       Ex	Excellent
       Gd	Good
       TA	Typical - slight dampness allowed
       Fa	Fair - dampness or some cracking or settling
       Po	Poor - Severe cracking, settling, or wetness
       NA	No Basement

BsmtExposure: Refers to walkout or garden level walls

       Gd	Good Exposure
       Av	Average Exposure (split levels or foyers typically score average or above)
       Mn	Mimimum Exposure
       No	No Exposure
       NA	No Basement

BsmtFinType1: Rating of basement finished area

       GLQ	Good Living Quarters
       ALQ	Average Living Quarters
       BLQ	Below Average Living Quarters
       Rec	Average Rec Room
       LwQ	Low Quality
       Unf	Unfinshed
       NA	No Basement

BsmtFinSF1: Type 1 finished square feet

BsmtFinType2: Rating of basement finished area (if multiple types)

       GLQ	Good Living Quarters
       ALQ	Average Living Quarters
       BLQ	Below Average Living Quarters
       Rec	Average Rec Room
       LwQ	Low Quality
       Unf	Unfinshed
       NA	No Basement

BsmtFinSF2: Type 2 finished square feet

BsmtUnfSF: Unfinished square feet of basement area

TotalBsmtSF: Total square feet of basement area

Heating: Type of heating

       Floor	Floor Furnace
       GasA	Gas forced warm air furnace
       GasW	Gas hot water or steam heat
       Grav	Gravity furnace
       OthW	Hot water or steam heat other than gas
       Wall	Wall furnace

HeatingQC: Heating quality and condition

       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       Po	Poor

CentralAir: Central air conditioning

       N	No
       Y	Yes

Electrical: Electrical system

       SBrkr	Standard Circuit Breakers & Romex
       FuseA	Fuse Box over 60 AMP and all Romex wiring (Average)
       FuseF	60 AMP Fuse Box and mostly Romex wiring (Fair)
       FuseP	60 AMP Fuse Box and mostly knob & tube wiring (poor)
       Mix	Mixed

1stFlrSF: First Floor square feet

2ndFlrSF: Second floor square feet

LowQualFinSF: Low quality finished square feet (all floors)

GrLivArea: Above grade (ground) living area square feet

BsmtFullBath: Basement full bathrooms

BsmtHalfBath: Basement half bathrooms

FullBath: Full bathrooms above grade

HalfBath: Half baths above grade

Bedroom: Bedrooms above grade (does NOT include basement bedrooms)

Kitchen: Kitchens above grade

KitchenQual: Kitchen quality

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor

TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)

Functional: Home functionality (Assume typical unless deductions are warranted)

       Typ	Typical Functionality
       Min1	Minor Deductions 1
       Min2	Minor Deductions 2
       Mod	Moderate Deductions
       Maj1	Major Deductions 1
       Maj2	Major Deductions 2
       Sev	Severely Damaged
       Sal	Salvage only

Fireplaces: Number of fireplaces

FireplaceQu: Fireplace quality

       Ex	Excellent - Exceptional Masonry Fireplace
       Gd	Good - Masonry Fireplace in main level
       TA	Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement
       Fa	Fair - Prefabricated Fireplace in basement
       Po	Poor - Ben Franklin Stove
       NA	No Fireplace

GarageType: Garage location

       2Types	More than one type of garage
       Attchd	Attached to home
       Basment	Basement Garage
       BuiltIn	Built-In (Garage part of house - typically has room above garage)
       CarPort	Car Port
       Detchd	Detached from home
       NA	No Garage

GarageYrBlt: Year garage was built

GarageFinish: Interior finish of the garage

       Fin	Finished
       RFn	Rough Finished
       Unf	Unfinished
       NA	No Garage

GarageCars: Size of garage in car capacity

GarageArea: Size of garage in square feet

GarageQual: Garage quality

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       NA	No Garage

GarageCond: Garage condition

       Ex	Excellent
       Gd	Good
       TA	Typical/Average
       Fa	Fair
       Po	Poor
       NA	No Garage

PavedDrive: Paved driveway

       Y	Paved
       P	Partial Pavement
       N	Dirt/Gravel

WoodDeckSF: Wood deck area in square feet

OpenPorchSF: Open porch area in square feet

EnclosedPorch: Enclosed porch area in square feet

3SsnPorch: Three season porch area in square feet

ScreenPorch: Screen porch area in square feet

PoolArea: Pool area in square feet

PoolQC: Pool quality

       Ex	Excellent
       Gd	Good
       TA	Average/Typical
       Fa	Fair
       NA	No Pool

Fence: Fence quality


> Indented block


       GdPrv	Good Privacy
       MnPrv	Minimum Privacy
       GdWo	Good Wood
       MnWw	Minimum Wood/Wire
       NA	No Fence

MiscFeature: Miscellaneous feature not covered in other categories

       Elev	Elevator
       Gar2	2nd Garage (if not described in garage section)
       Othr	Other
       Shed	Shed (over 100 SF)
       TenC	Tennis Court
       NA	None

MiscVal: $Value of miscellaneous feature

MoSold: Month Sold (MM)

YrSold: Year Sold (YYYY)

SaleType: Type of sale

       WD 	Warranty Deed - Conventional
       CWD	Warranty Deed - Cash
       VWD	Warranty Deed - VA Loan
       New	Home just constructed and sold
       COD	Court Officer Deed/Estate
       Con	Contract 15% Down payment regular terms
       ConLw	Contract Low Down payment and low interest
       ConLI	Contract Low Interest
       ConLD	Contract Low Down
       Oth	Other

SaleCondition: Condition of sale

       Normal	Normal Sale
       Abnorml	Abnormal Sale -  trade, foreclosure, short sale
       AdjLand	Adjoining Land Purchase
       Alloca	Allocation - two linked properties with separate deeds, typically condo with a garage unit
       Family	Sale between family members
       Partial	Home was not completed when last assessed (associated with New Homes)


The dataset is uploaded in the google drive and can be used in our workspace.
"""

from google.colab import drive
drive.mount('/content/gdrive')

"""

**1**.   **INITIALIZING THE DATASET**

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=pd.read_csv("/content/gdrive/MyDrive/FML MINI PROJECT/DATASET/train.csv")
a

df1=a.drop("Id", axis='columns')

df1

"""**2**.    **DATA** **PREPROCESSING**"""

df1.info()

df1['MSZoning'].unique()

from sklearn import preprocessing

# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column of every object type columns.
df1['MSZoning']= label_encoder.fit_transform(df1['MSZoning'])
df1['Street']= label_encoder.fit_transform(df1['Street'])
df1['Alley']= label_encoder.fit_transform(df1['Alley'])
df1['LotShape']= label_encoder.fit_transform(df1['LotShape'])
df1['LandContour']= label_encoder.fit_transform(df1['LandContour'])
df1['Utilities']= label_encoder.fit_transform(df1['Utilities'])
df1['LotConfig']= label_encoder.fit_transform(df1['LotConfig'])
df1['LandSlope']= label_encoder.fit_transform(df1['LandSlope'])
df1['Neighborhood']= label_encoder.fit_transform(df1['Neighborhood'])
df1['Condition1']= label_encoder.fit_transform(df1['Condition1'])
df1['Condition2']= label_encoder.fit_transform(df1['Condition2'])
df1['BldgType']= label_encoder.fit_transform(df1['BldgType'])
df1['HouseStyle']= label_encoder.fit_transform(df1['HouseStyle'])
df1['RoofStyle']= label_encoder.fit_transform(df1['RoofStyle'])
df1['RoofMatl']= label_encoder.fit_transform(df1['RoofMatl'])
df1['Exterior1st']= label_encoder.fit_transform(df1['Exterior1st'])
df1['Exterior2nd']= label_encoder.fit_transform(df1['Exterior2nd'])
df1['MasVnrType']= label_encoder.fit_transform(df1['MasVnrType'])
df1['ExterQual']= label_encoder.fit_transform(df1['ExterQual'])
df1['ExterCond']= label_encoder.fit_transform(df1['ExterCond'])
df1['Foundation']= label_encoder.fit_transform(df1['Foundation'])
df1['BsmtQual']= label_encoder.fit_transform(df1['BsmtQual'])
df1['BsmtCond']= label_encoder.fit_transform(df1['BsmtCond'])
df1['BsmtExposure']= label_encoder.fit_transform(df1['BsmtExposure'])
df1['BsmtFinType1']= label_encoder.fit_transform(df1['BsmtFinType1'])
df1['BsmtFinType2']= label_encoder.fit_transform(df1['BsmtFinType2'])
df1['Heating']= label_encoder.fit_transform(df1['Heating'])
df1['HeatingQC']= label_encoder.fit_transform(df1['HeatingQC'])
df1['CentralAir']= label_encoder.fit_transform(df1['CentralAir'])
df1['Electrical']= label_encoder.fit_transform(df1['Electrical'])
df1['KitchenQual']= label_encoder.fit_transform(df1['KitchenQual'])
df1['Functional']= label_encoder.fit_transform(df1['Functional'])
df1['FireplaceQu']= label_encoder.fit_transform(df1['FireplaceQu'])
df1['GarageType']= label_encoder.fit_transform(df1['GarageType'])
df1['GarageFinish']= label_encoder.fit_transform(df1['GarageFinish'])
df1['GarageQual']= label_encoder.fit_transform(df1['GarageQual'])
df1['GarageCond']= label_encoder.fit_transform(df1['GarageCond'])
df1['PavedDrive']= label_encoder.fit_transform(df1['PavedDrive'])
df1['PoolQC']= label_encoder.fit_transform(df1['PoolQC'])
df1['Fence']= label_encoder.fit_transform(df1['Fence'])
df1['MiscFeature']= label_encoder.fit_transform(df1['MiscFeature'])
df1['SaleType']= label_encoder.fit_transform(df1['SaleType'])
df1['SaleCondition']= label_encoder.fit_transform(df1['SaleCondition'])

df1.info()

df1['MSZoning'].unique()

df1=df1.fillna(100)
df1

"""**3. DATA ANALYSIS FOR PREDICTION**

since the dataset contains 79 input variables let us take the top 10 features which determines the SalePrice and let's graph
"""

sb.pairplot(data=df1[['LotFrontage','TotalBsmtSF','BsmtUnfSF','SalePrice']],x_vars=['LotFrontage','TotalBsmtSF','BsmtUnfSF'],y_vars='SalePrice')
plt.show()

sb.pairplot(data=df1[['GarageArea','1stFlrSF','LotArea','GrLivArea','SalePrice']],x_vars=['GarageArea','1stFlrSF','LotArea','GrLivArea'],y_vars='SalePrice')
plt.show()

"""**4. PREDICTION**

**4.1 LINEAR REGRESSION**
"""

x=df1.drop(['SalePrice'],axis='columns')
y=df1['SalePrice']

x

y

from sklearn import linear_model
lr1 = linear_model.LinearRegression()
lr1.fit(x,y)

coeffs1 = pd.DataFrame(lr1.coef_,x.columns,columns=['Coefficient'])
coeffs1

pred1 = lr1.predict(x)

scores1 = pd.DataFrame({'Actual':y,'Predictions':pred1})
g=sb.pairplot(data=scores1[['Actual','Predictions']],x_vars=['Actual'],y_vars='Predictions')
g.fig.set_figheight(6)
g.fig.set_figwidth(10)
plt.title("Actual VS Prediction")
plt.show()

from sklearn import metrics
print(np.sqrt(metrics.mean_squared_error(y,pred1)))
print(y.mean)
print(metrics.r2_score(y,pred1))

"""**4.2 RANDOM FOREST FOR PREDICTION**

We have to find best n_estimators for our random forest to predict the values properly. There is an in-built function for this provided y the GridSearchCV package

from sklearn.model_selection import GridSearchCV

model=RandomForestClassifier()

params={'n_estimators':range(1,200)}

grid=GridSearchCV(estimator=model,cv=2,param_grid=params,scoring='neg_mean_squared_error')

grid.fit(x,y)

print("The best estimator returned by GridSearch CV is:",grid.best_estimator_)

**OUTPUT**

/usr/local/lib/python3.7/dist-packages/sklearn/model_selection/_split.py:680: UserWarning: The least populated class in y has only 1 members, which is less than n_splits=2.

  UserWarning,

The best estimator returned by GridSearch CV is: RandomForestClassifier(n_estimators=162)
"""

from sklearn.ensemble import RandomForestClassifier
modelr=RandomForestClassifier(n_estimators=162)
modelr.fit(x,y)

y_predict2=modelr.predict(x)
y_predict2

scores1 = pd.DataFrame({'Actual':y,'Predictions':y_predict2})
g=sb.pairplot(data=scores1[['Actual','Predictions']],x_vars=['Actual'],y_vars='Predictions')
g.fig.set_figheight(6)
g.fig.set_figwidth(10)
plt.title("Actual VS Prediction")
plt.show()

g=sb.pairplot(data=scores1[['Actual','Predictions']],x_vars=['Actual'],y_vars='Predictions')
g.fig.set_figheight(6)
g.fig.set_figwidth(10)
plt.title("Actual VS Prediction")
plt.show()

from sklearn import metrics
import numpy as np
print(np.sqrt(metrics.mean_squared_error(y,y_predict2)))
print(y.mean)
print(metrics.r2_score(y,y_predict2))

"""**4.3 GRADIENT BOOSTING FOR PREDICTION**

Like random forest we can also find best n_estimators for the GradientBoostingRegressor by using GridSearchCV package

from sklearn.model_selection import GridSearchCV

model=GradientBoostingRegressor()

params={'n_estimators':range(1,200)}

grid=GridSearchCV(estimator=model,cv=2,param_grid=params,scoring='neg_mean_squared_error')

grid.fit(x,y)

print("The best estimator returned by GridSearch CV is:",grid.best_estimator_)

**OUTPUT**

/usr/local/lib/python3.7/dist-packages/sklearn/model_selection/_split.py:680: UserWarning: The least populated class in y has only 1 members, which is less than n_splits=2.

  UserWarning,
  
The best estimator returned by GridSearch CV is: RandomForestClassifier(n_estimators=154)
"""

from sklearn.ensemble import GradientBoostingRegressor
modelg=GradientBoostingRegressor(n_estimators=154)
modelg.fit(x,y)

y_predict3=modelg.predict(x)
y_predict3

scores1 = pd.DataFrame({'Actual':y,'Predictions':y_predict3})
g=sb.pairplot(data=scores1[['Actual','Predictions']],x_vars=['Actual'],y_vars='Predictions')
g.fig.set_figheight(6)
g.fig.set_figwidth(10)
plt.title("Actual VS Prediction")
plt.show()

from sklearn import metrics
import numpy as np
print(np.sqrt(metrics.mean_squared_error(y,y_predict3)))
print(y.mean)
print(metrics.r2_score(y,y_predict3))

df1['SalePrice'].max()

df1['SalePrice'].min()

"""Now we are going to do feature extraction for prediction

**5. FEATURE EXTRACTION FOR PREDICTION**
"""

feature_importance=pd.DataFrame(modelr.feature_importances_,index=x.columns,columns=['importance']).sort_values('importance')
feature_importance.head(20)

feature_importance.head(20).sum()

feature_importance.tail(59)

feature_importance.tail(51).sum()

"""Now, analyzing the feature extraction we are going to importance columns which is above the value of 0.010000"""

xf=df1[['Functional','BldgType','LandContour','BsmtCond','ExterCond','ExterQual','FullBath','BsmtFinType2','ScreenPorch','HalfBath','SaleType','MSZoning','RoofStyle','Foundation','GarageCars','BsmtFinSF2','Fence','BsmtFullBath','KitchenQual','SaleCondition','GarageType','Condition1','BsmtQual','EnclosedPorch','LotShape','Fireplaces','HouseStyle','LotConfig','HeatingQC','MasVnrType','GarageFinish','BsmtExposure','MSSubClass','FireplaceQu','BedroomAbvGr','OverallCond','BsmtFinType1','OverallQual','Exterior1st','Exterior2nd','2ndFlrSF','TotRmsAbvGrd','MasVnrArea','YrSold','Neighborhood','WoodDeckSF','OpenPorchSF','BsmtFinSF1','YearRemodAdd','MoSold','GarageYrBlt','YearBuilt','LotFrontage','TotalBsmtSF','GarageArea','1stFlrSF','BsmtUnfSF','LotArea','GrLivArea']]
yf=df1['SalePrice']

"""**5.1 LINEAR REGRESSION**"""

from sklearn import linear_model
lrf = linear_model.LinearRegression()
lrf.fit(xf,yf)

coeffsf = pd.DataFrame(lrf.coef_,xf.columns,columns=['Coefficient'])
coeffsf

predf = lrf.predict(xf)

scoresf = pd.DataFrame({'Actual':yf,'Predictions':predf})
g=sb.pairplot(data=scoresf[['Actual','Predictions']],x_vars=['Actual'],y_vars='Predictions')
g.fig.set_figheight(6)
g.fig.set_figwidth(10)
plt.title("Actual VS Prediction")
plt.show()

from sklearn import metrics
print(np.sqrt(metrics.mean_squared_error(yf,predf)))
print(yf.mean)
print(metrics.r2_score(yf,predf))

"""**5.2 RANDOM FOREST**"""

from sklearn.ensemble import RandomForestClassifier
modelrf=RandomForestClassifier(n_estimators=162)
modelrf.fit(xf,yf)

y_predictf1=modelrf.predict(xf)
y_predictf1

scoresf1 = pd.DataFrame({'Actual':yf,'Predictions':y_predictf1})
g=sb.pairplot(data=scoresf1[['Actual','Predictions']],x_vars=['Actual'],y_vars='Predictions')
g.fig.set_figheight(6)
g.fig.set_figwidth(10)
plt.title("Actual VS Prediction")
plt.show()

from sklearn import metrics
import numpy as np
print(np.sqrt(metrics.mean_squared_error(yf,y_predictf1)))
print(yf.mean)
print(metrics.r2_score(yf,y_predictf1))

"""**5.3 GRADIENT BOOSTING**"""

from sklearn.ensemble import GradientBoostingRegressor
modelgf=GradientBoostingRegressor(n_estimators=154)
modelgf.fit(xf,yf)

y_predictf2=modelgf.predict(xf)
y_predictf2

scoresf2 = pd.DataFrame({'Actual':yf,'Predictions':y_predictf2})
g=sb.pairplot(data=scoresf2[['Actual','Predictions']],x_vars=['Actual'],y_vars='Predictions')
g.fig.set_figheight(6)
g.fig.set_figwidth(10)
plt.title("Actual VS Prediction")
plt.show()

from sklearn import metrics
import numpy as np
print(np.sqrt(metrics.mean_squared_error(yf,y_predictf2)))
print(yf.mean)
print(metrics.r2_score(yf,y_predictf2))

"""**6. CONERTING INTO CATEGORICAL VALUE**

Now, we are going add a new column based on the SalePrice attribute from the dataset and name the resultant attribute as SalesType

SalesType attribute description

A - Price less than 200000

B - Price greater than or equal to 200000 and less than 400000

C - Price greater than or equal to 400000 and less than 600000

H - Price greater than 600000
"""

def myfunc(SalePrice):
    if SalePrice<200000:
        Type='A'
    elif SalePrice>=200000 and SalePrice<400000:
        Type='B'
    elif SalePrice>=400000 and SalePrice<600000:
        Type='C'
    else:
        Type='H'
    return Type

df1['SalesType'] = df1.apply(lambda x: myfunc(x['SalePrice']), axis=1)

df1

df1['SalesType'].value_counts()

"""Now, we are going to assign the independent variable namely as lx1 and dependent variable namely as ly1 which is commonly used for all models"""

lx1=df1.drop(['SalePrice','SalesType'],axis=1)
ly1=df1['SalesType']

lx1.shape

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(lx1,ly1,test_size=0.20,random_state=1)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

"""**DATA ANALYSIS FOR CATEGORICAL**"""

import matplotlib.pyplot as plt
import seaborn as sns
y = df1['SalesType']
ax = sns.countplot(df1['SalesType'])
SalesType_temp = df1.SalesType.value_counts()
print(SalesType_temp)

print("Percentage of price from 0 to 200000 : {}%".format(str(round(SalesType_temp[0]*100/1460,2))))
print("Percentage of price from 200000 to 400000 : {}%".format(str(round(SalesType_temp[1]*100/1460,2))))
print("Percentage of price from 400000 to 600000 : {}%".format(str(round(SalesType_temp[2]*100/1460,2))))
print("Percentage of price greater than 600000 : {}%".format(str(round(SalesType_temp[3]*100/1460,2))))

pd.crosstab(df1.YearBuilt,df1.SalesType).plot(kind="bar",figsize=(30,12))
plt.title('HOUSE SALE PRICE BY ORGINAL CONSTRUCTION YEAR')
plt.xlabel('YEAR BUILT')
plt.ylabel('HOUSE PRICE')
plt.savefig('housepriceandyearbuilt.png')
plt.show()

"""**6.1 LOGISTIC REGRESSION MODEL**"""

from sklearn.linear_model import LogisticRegression
Classifier=LogisticRegression(solver='liblinear')
Classifier.fit(x_train,y_train)

y_pred2=Classifier.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred2})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred2))

"""**6.2 K-NEAREST NEIGHBOUR ALGORITHM**"""

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)

y_pred3=model.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred3})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm1=confusion_matrix(y_test,y_pred3)
plt.figure(figsize=(1,1))
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm1 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred3))

"""**6.3 DECISION TREE ALGORITHM**"""

from sklearn.tree import DecisionTreeClassifier
model1=DecisionTreeClassifier()
model1.fit(x_train,y_train)

y_pred4=model1.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred4})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm2=confusion_matrix(y_test,y_pred4)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm2 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred4))

"""**6.4 NAIVE BAYES ALGORITH [GAUSSIANNB]**"""

from sklearn.naive_bayes import GaussianNB
model2=GaussianNB()
model2.fit(x_train,y_train)

y_pred5=model2.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred5})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm3=confusion_matrix(y_test,y_pred5)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm3 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred5))

"""**6.5 ENSEMBLE ALGORITHM [RANDOM FOREST]**"""

from sklearn.ensemble import RandomForestClassifier
model3=RandomForestClassifier(n_estimators=198)
model3.fit(x_train,y_train)

y_pred6=model3.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred6})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm4=confusion_matrix(y_test,y_pred6)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm4 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred6))

"""**6.6 XGBOOST [XGBCLASSIFIER]**"""

from xgboost import XGBClassifier
model4=XGBClassifier()
model4.fit(x_train,y_train)

y_pred7=model4.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred7})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm5=confusion_matrix(y_test,y_pred7)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm5 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred7))

"""Now, we are going to do feature extraction for categorical values

**7. FEATURE EXTRACTION FOR CATEGORICAL**
"""

feature_importance1=pd.DataFrame(model3.feature_importances_,index=x_train.columns,columns=['importance']).sort_values('importance')
feature_importance1.head(18)

feature_importance1.head(18).sum()

xc=df1.drop(['Street','Utilities','GarageCond','PoolQC','Condition2','Heating','PoolArea','CentralAir','LowQualFinSF','MiscVal','MiscFeature','Electrical','PavedDrive','BsmtHalfBath','3SsnPorch','GarageQual','KitchenAbvGr','ExterCond','SalePrice','SalesType'],axis=1)
yc=df1['SalesType']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(xc,yc,test_size=0.20,random_state=1)

"""**7.1 LOGISTIC REGRESSION**"""

from sklearn.linear_model import LogisticRegression
Classifierf=LogisticRegression(solver='liblinear')
Classifierf.fit(x_train,y_train)

y_pred2f=Classifierf.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred2f})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred2f))

"""**7.2 K-NEAREST NEIGHBOUR**"""

from sklearn.neighbors import KNeighborsClassifier
modelf=KNeighborsClassifier(n_neighbors=5)
modelf.fit(x_train,y_train)

y_pred3f=modelf.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred3f})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm1=confusion_matrix(y_test,y_pred3f)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm1 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred3f))

"""**7.3 DECISION TREE**"""

from sklearn.tree import DecisionTreeClassifier
model1f=DecisionTreeClassifier()
model1f.fit(x_train,y_train)

y_pred4f=model1f.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred4f})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm2=confusion_matrix(y_test,y_pred4f)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm2 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred4f))

"""**7.4 GAUSSIANNB**"""

from sklearn.naive_bayes import GaussianNB
model2f=GaussianNB()
model2f.fit(x_train,y_train)

y_pred5f=model2f.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred5f})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm3=confusion_matrix(y_test,y_pred5f)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm3 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred5))

"""**7.5 RANDOM FOREST**"""

from sklearn.ensemble import RandomForestClassifier
model3f=RandomForestClassifier(n_estimators=198)
model3f.fit(x_train,y_train)

y_pred6f=model3f.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred6f})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm4=confusion_matrix(y_test,y_pred6f)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm4 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred6f))

"""**7.6 XGBCLASSIFIER**"""

from xgboost import XGBClassifier
model4f=XGBClassifier()
model4f.fit(x_train,y_train)

y_pred7f=model4f.predict(x_test)
results=pd.DataFrame({'Actual':y_test,'Predictions':y_pred7f})
pd.crosstab(results.Actual,results.Predictions).plot(kind="bar",figsize=(5,5))
plt.title('Actual VS Predictions')
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.show()

from sklearn.metrics import confusion_matrix
cm5=confusion_matrix(y_test,y_pred7f)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm5 , display_labels = ['A','B','C','H'])
cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred7f))

"""By, the above codes that we can conclude that the random forest for prediction is best suitable for the house prediction dataset.

The given dataset that had been downloaded from kaggle had already splitted the dataset into training and testing dataset.

And the testing dataset doesn't contains the dependent variable i.e) the output variable y.

Let's predict the y variable i.e) SalePrice of the testing dataset
"""

b=pd.read_csv('/content/gdrive/MyDrive/FML MINI PROJECT/DATASET/test.csv')
b

df2=b.drop('Id',axis=1)
id=b['Id']

df2

"""Now, we are going to do data preprocessing for test data

"""

from sklearn import preprocessing

# label_encoder object knows how to understand word labels.
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column of every object type columns.
df2['MSZoning']= label_encoder.fit_transform(df2['MSZoning'])
df2['Street']= label_encoder.fit_transform(df2['Street'])
df2['Alley']= label_encoder.fit_transform(df2['Alley'])
df2['LotShape']= label_encoder.fit_transform(df2['LotShape'])
df2['LandContour']= label_encoder.fit_transform(df2['LandContour'])
df2['Utilities']= label_encoder.fit_transform(df2['Utilities'])
df2['LotConfig']= label_encoder.fit_transform(df2['LotConfig'])
df2['LandSlope']= label_encoder.fit_transform(df2['LandSlope'])
df2['Neighborhood']= label_encoder.fit_transform(df2['Neighborhood'])
df2['Condition1']= label_encoder.fit_transform(df2['Condition1'])
df2['Condition2']= label_encoder.fit_transform(df2['Condition2'])
df2['BldgType']= label_encoder.fit_transform(df2['BldgType'])
df2['HouseStyle']= label_encoder.fit_transform(df2['HouseStyle'])
df2['RoofStyle']= label_encoder.fit_transform(df2['RoofStyle'])
df2['RoofMatl']= label_encoder.fit_transform(df2['RoofMatl'])
df2['Exterior1st']= label_encoder.fit_transform(df2['Exterior1st'])
df2['Exterior2nd']= label_encoder.fit_transform(df2['Exterior2nd'])
df2['MasVnrType']= label_encoder.fit_transform(df2['MasVnrType'])
df2['ExterQual']= label_encoder.fit_transform(df2['ExterQual'])
df2['ExterCond']= label_encoder.fit_transform(df2['ExterCond'])
df2['Foundation']= label_encoder.fit_transform(df2['Foundation'])
df2['BsmtQual']= label_encoder.fit_transform(df2['BsmtQual'])
df2['BsmtCond']= label_encoder.fit_transform(df2['BsmtCond'])
df2['BsmtExposure']= label_encoder.fit_transform(df2['BsmtExposure'])
df2['BsmtFinType1']= label_encoder.fit_transform(df2['BsmtFinType1'])
df2['BsmtFinType2']= label_encoder.fit_transform(df2['BsmtFinType2'])
df2['Heating']= label_encoder.fit_transform(df2['Heating'])
df2['HeatingQC']= label_encoder.fit_transform(df2['HeatingQC'])
df2['CentralAir']= label_encoder.fit_transform(df2['CentralAir'])
df2['Electrical']= label_encoder.fit_transform(df2['Electrical'])
df2['KitchenQual']= label_encoder.fit_transform(df2['KitchenQual'])
df2['Functional']= label_encoder.fit_transform(df2['Functional'])
df2['FireplaceQu']= label_encoder.fit_transform(df2['FireplaceQu'])
df2['GarageType']= label_encoder.fit_transform(df2['GarageType'])
df2['GarageFinish']= label_encoder.fit_transform(df2['GarageFinish'])
df2['GarageQual']= label_encoder.fit_transform(df2['GarageQual'])
df2['GarageCond']= label_encoder.fit_transform(df2['GarageCond'])
df2['PavedDrive']= label_encoder.fit_transform(df2['PavedDrive'])
df2['PoolQC']= label_encoder.fit_transform(df2['PoolQC'])
df2['Fence']= label_encoder.fit_transform(df2['Fence'])
df2['MiscFeature']= label_encoder.fit_transform(df2['MiscFeature'])
df2['SaleType']= label_encoder.fit_transform(df2['SaleType'])
df2['SaleCondition']= label_encoder.fit_transform(df2['SaleCondition'])

df2=df2.fillna(100)

df2.info()

y_predict1=modelr.predict(df2)
y_predict1

result = pd.DataFrame({'Id':id,'SalePrice':y_predict1})
result.head(30)

result['SalePrice'].max()

result['SalePrice'].min()

"""Now, we are going to download the resultant dataframe called **result** as a CSV file"""

from google.colab import files
result.to_csv('final.csv')
files.download('final.csv')
