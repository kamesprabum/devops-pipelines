console.log("Starting test...");
setTimeout(() => console.log("Waiting 3S...."), 3000);
console.log("Test completed.");
throw new Error("I intentionally broke the test!");