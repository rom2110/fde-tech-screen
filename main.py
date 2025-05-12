from package import Package
import csv

def sort(width, height, length, mass):
    package = Package(width, height, length, mass)
    return package.get_stack_name()

def test_code(tests : list[int]):
    failed_cases = []

    for test in tests:
        ((width, height, length, mass), expected_result) = test
        result = sort(width, height, length, mass)
        if result != expected_result:
            failed_cases.append((test, result))

    return failed_cases

def test_exceptions(tests : list):
    failed = []
    passed = []

    for test in tests:
        try:
            if len(test) != 4:
                raise Exception("Input is not the correct length")
            width, height, length, mass = test
            sort(int(width), int(height), int(length), int(mass))
            passed.append(test)
        except Exception as e:
            failed.append((test, e))

    return {"passed": passed, "failed": failed}

if __name__ == "__main__":
    list = [
        
        #Should pass
        ((10,20,40, 2), "STANDARD"),
        ((5, 5, 5, 5), "STANDARD"),

        #Special because of length
        ((150, 10, 10, 15), "SPECIAL"),
        ((150, 150, 5, 10), "SPECIAL"),
        
        #Special because of volume
        ((100, 100, 100, 5), "SPECIAL"),
        ((100, 140, 100, 10), "SPECIAL"),

        #Special because of weight
        ((140, 140, 20, 20), "SPECIAL"),
        ((30, 50, 80, 25), "SPECIAL"),

        #Rejected because bulky and heavy
        ((1000, 100, 10, 20), "REJECTED"),
        ((1000, 150, 10, 20), "REJECTED"),
        ((1000, 100, 10, 25), "REJECTED"),
        ((1000, 150, 10, 25), "REJECTED"),
        
    ]

    failed_cases = test_code(list)
    if len(failed_cases)> 0:
        print(f"FAILED {len(failed_cases)} TEST CASES:")
        print(failed_cases)
    else:
        print("PASSED ALL TEST CASES")

    with open('packages.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
        
    results = test_exceptions(data)
    print(f"NO EXCEPTIONS:\n")
    for test in results['passed']:
        print(test)
    print(f"EXCEPTIONS FOUND:\n")
    for test in results['failed']:
        print(test)