package cars

// CalculateWorkingCarsPerHour calculates how many working cars are produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	return float64(productionRate) * (successRate / 100.0)
}

// CalculateWorkingCarsPerMinute calculates how many working cars are produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	return int(CalculateWorkingCarsPerHour(productionRate, successRate) / 60)
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	const bulkSize = 10
	const bulkPrice = 95000 // 10 cars for $95,000
	const singleCarPrice = 10000

	bulkCars := carsCount / bulkSize
	remainingCars := carsCount % bulkSize

	return uint(bulkCars*bulkPrice + remainingCars*singleCarPrice)
}
