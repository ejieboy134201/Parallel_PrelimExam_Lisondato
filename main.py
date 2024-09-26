import serial_convolution
import parallel_convolution
import time

def main():
    image_folder = 'dog_train'  # Folder where your dog images are stored
    
    # Ask the user for number of iterations
    num_iterations = int(input("Please input number of iterations: "))
    
    # Initialize lists to store results
    results = []
    
    # Run for each iteration
    for iteration in range(num_iterations):
        # Ask the user how many images to process in this iteration
        num_images = int(input(f"Please input number of images for iteration {iteration + 1}: "))
        
        # Process images serially
        serial_time = serial_convolution.process_images_serial(image_folder, num_images)
        
        # Process images in parallel
        parallel_time = parallel_convolution.process_images_parallel(image_folder, num_images)
        
        # Calculate speedup (serial / parallel)
        speedup = serial_time / parallel_time if parallel_time > 0 else float('inf')
        
        # Store the result in a dictionary
        results.append({
            'Iteration': iteration + 1,
            'Images': num_images,
            'Serial Time (ms)': round(serial_time, 4),
            'Parallel Time (ms)': round(parallel_time, 4),
            'Speedup': round(speedup, 4)
        })
    
    # Display the results in table format
    print("\nResults Table:")
    print("{:<10} {:<10} {:<20} {:<20} {:<10}".format('Iteration', 'Images', 'Serial Time (ms)', 'Parallel Time (ms)', 'Speedup'))
    for result in results:
        print("{:<10} {:<10} {:<20} {:<20} {:<10}".format(result['Iteration'], result['Images'], result['Serial Time (ms)'], result['Parallel Time (ms)'], result['Speedup']))

if __name__ == "__main__":
    main()
