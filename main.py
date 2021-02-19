import slidetemplater.api

def main():
    result = slidetemplater.api.convert(open(
        'covid.pptx', 'rb'), "https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=cumPeopleVaccinatedFirstDoseByVaccinationDate&format=json")

    f = open('result.pptx', 'w+b')
    f.write(result)
    f.close()

if __name__ == "__main__":
    main()