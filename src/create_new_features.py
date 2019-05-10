import pandas as pd
import os


def region_by_country(country):
    """Get region using the country"""
    region_by_country = ''
    return region_by_country


def age_range(age):
    try:
        age = int(age)
        if age < 18:
            age_range = 'ar < 18'
        elif age < 27:
            age_range = 'ar 18 - 26'
        elif age < 37:
            age_range = 'ar 27 - 36'
        elif age < 51:
            age_range = 'ar 37 - 50'
        elif age < 66:
            age_range = 'ar 51 - 60'
        elif age > 64:
            age_range = 'ar 65+'
        else:
            age_range = 'ar unknown'
    except Exception as e:
        age_range = 'ar unknown'
    return age_range


def new_target(df):
    if df.new_user == 1 and df.converted == 1:
        target = 'converted_at_first_visit'
    elif df.new_user == 0 and df.converted == 1:
        target = 'converted_not_at_first'
    else:
        target = 'did_not_convert'
    return target


def main():
    # load the file and do some basic exploration
    path = '/Users/youval.dar/Documents/other_things/general/cb/data'
    df = pd.read_csv(os.path.join(path, 'conversion_data.csv'))
    # df['region'] = df.country.apply(region_by_country)
    df['age_range'] = df.age.apply(age_range)
    # look at new data
    print(df.head())
    # write new data
    df.to_csv(os.path.join(path, 'conversion_data_with_extra_feature_2.csv'), index=False)

    # create a different target
    # write new data
    print('Create new target...')
    df['target'] = df.apply(new_target, axis=1)
    # Removing the converted column so that it will not bias the model
    df = df.drop(columns=['converted'])
    print(df.head())
    df.to_csv(os.path.join(path, 'conversion_data_with_extra_feature_1.csv'), index=False)


if __name__ == '__main__':
    main()

