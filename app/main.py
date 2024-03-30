from pipeline import extract, transform, load


if __name__ == "__main__":

    input_path = './data/input'

    df = extract.extract_from_excel(input_path)

    df = transform.transform_dataframe(df)

    output_path = './data/output'
    file_name_output = 'output.xlsx'

    load.load_dataframe(df, output_path, file_name_output)
