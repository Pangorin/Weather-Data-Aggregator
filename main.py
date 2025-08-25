from scripts import extract
from scripts import transform
from scripts import load

def run_pipeline():
    # Execute whole ETL pipeline in sequence.
    print("Weather ETL pipeline started.")

    try:
        print("Phase 1: Extract")
        extract.run()
        print("Extract complete. \n")

        print("Phase 2: Transform")
        transform.run()
        print("Transform completed. \n")

        print("Phase 3: Load")
        load.run()
        print("Load complete. \n")

        print("Whole process executed successfully. \n")

    except Exception as e:
        print("\n" + "="*50)
        print("Pipeline failed.")
        print(f"Error: {e}")
        print("="*50)

if __name__ == "__main__":
    run_pipeline()