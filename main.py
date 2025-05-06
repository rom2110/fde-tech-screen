from package import Package

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