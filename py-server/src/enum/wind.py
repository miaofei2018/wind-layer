"""
使用eccodes解析需要的字段
"""
def WindEnum():
    return [
        "discipline",
        "editionNumber",
        "centre",
        "subCentre",
        "significanceOfReferenceTime",
        "dataDate",
        "dataTime",
        "productionStatusOfProcessedData",
        "typeOfProcessedData",
        "numberOfDataPoints",
        "interpretationOfNumberOfPoints",
        "gridDefinitionTemplateNumber",
        "shapeOfTheEarth",
        "Ni",
        "Nj",
        "iScansNegatively",
        "jScansPositively",
        "jPointsAreConsecutive",
        "alternativeRowScanning",
        "latitudeOfFirstGridPointInDegrees",
        "longitudeOfFirstGridPointInDegrees",
        "latitudeOfLastGridPointInDegrees",
        "longitudeOfLastGridPointInDegrees",
        "iDirectionIncrementInDegrees",
        "jDirectionIncrementInDegrees",
        "gridType",
        "NV",
        "productDefinitionTemplateNumber",
        "parameterCategory",
        "parameterNumber",
        "parameterUnits",
        "parameterName",
        "typeOfGeneratingProcess",
        "generatingProcessIdentifier",
        "indicatorOfUnitOfTimeRange",
        "stepUnits",
        "forecastTime",
        "stepRange",
        "typeOfFirstFixedSurface",
        "unitsOfFirstFixedSurface",
        "nameOfFirstFixedSurface",
        "scaleFactorOfFirstFixedSurface",
        "scaledValueOfFirstFixedSurface",
        "typeOfSecondFixedSurface",
        "unitsOfSecondFixedSurface",
        "nameOfSecondFixedSurface",
        "scaleFactorOfSecondFixedSurface",
        "scaledValueOfSecondFixedSurface",
        "level",
        "shortNameECMF",
        "shortName",
        "nameECMF",
        "name",
        "cfNameECMF",
        "cfName",
        "cfVarNameECMF",
        "cfVarName",
        "modelName",
        "numberOfValues",
        "packingType",
        "bitMapIndicator",
        "bitmapPresent"
    ]


"""
使用 `rasterio` 需要的结果字段
"""
def WindJSON():
  return [
    ''
  ]
