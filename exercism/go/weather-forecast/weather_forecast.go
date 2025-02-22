// Package weather provides tools to convert
// temperatures to and from Kelvin.
package weather

// CurrentCondition a var to invoke where is cold/warm/or something else ...etc.
var CurrentCondition string
// CurrentLocation a var to invoke where you are.
var CurrentLocation string

// Forecast a function to doing weather forecast.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
