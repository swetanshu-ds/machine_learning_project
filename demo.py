from housing.pipeline.pipeline import Pipeline
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        print()

if __name__ == "__main__":
    main()