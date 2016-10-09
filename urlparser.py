def parseURL(url):
    # assuming that there are no question marks within the params -- Tru
    urlParamsFull = url.split('?')[-1]

    # safe
    urlParams = urlParamsFull.split('&')
    urlTups = [tuple(urlParam.split('=')) for urlParam in urlParams]
    paramDict = {}
    for urlTup in urlTups:
        if len(urlTup) == 2:
            key, val = urlTup
            if key not in paramDict:
                paramDict[key] = val
            elif type(paramDict[key]) == list:
                paramDict[key].append(val)
            else:
                paramDict[key] = [paramDict[key], val]

    return paramDict

if __name__ == "__main__":
    url = "google.com/index.html?myfirstparam=1&mysecondparam=2"
    url1 = "google.com/index.html?"
    url2 = "google.com/index.html?myfarsdioj=1&"
    url3 = "google.com/index.html?mykey1=5&mykey1=8&mykey3=52342"
    print(parseURL(url))
    print(parseURL(url1))
    print(parseURL(url2))
    print(parseURL(url3))
