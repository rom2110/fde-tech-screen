from package import Package
class Factory:

    def __init__(self, input : list):
        self.packages = []
        for (width, height, length, mass) in input:
            self.packages.append(Package(width, height, length, mass))

    def total_processed_packages(self) -> int:
        return len(self.packages)
    
    #both percentage and counts of each stack
    def stack_statistics(self):
        countStan =  0
        countSpec = 0
        countRej = 0

        volume
        mass

        for package in self.packages:
            stack_name = package.get_stack_name()
            if stack_name == "STANDARD":
                countStan += 1
            if stack_name == "SPECIAL":
                countSpec += 1
            if stack_name == "REJECTED":
                countRej += 1
        total = self.total_processed_packages()
        return {
            'STANDARD': {'count': countStan, 'percentage': countStan/total}, 
            'SPECIAL': {'count': countSpec, 'percentage': countSpec/total}, 
            'REJECTED': {'count': countRej, 'percentage': countRej/total}
            }

    #returns average, min, max for mass and volume
    def statistcs(self):


    def generate_report(self):