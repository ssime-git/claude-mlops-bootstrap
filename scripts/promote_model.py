"""CLI script to promote or rollback models in MLflow Registry."""

import argparse
import sys

from fraud_detection.registry import promote_model, rollback_model


def main() -> None:
    """Parse args and promote/rollback model."""
    parser = argparse.ArgumentParser(description="Promote or rollback MLflow models")
    parser.add_argument(
        "--stage",
        choices=["staging", "production"],
        help="Target stage for promotion",
    )
    parser.add_argument(
        "--rollback",
        action="store_true",
        help="Rollback production to previous version",
    )
    parser.add_argument(
        "--version",
        type=str,
        default=None,
        help="Specific version to promote (default: latest)",
    )
    parser.add_argument(
        "--model-name",
        type=str,
        default="FraudDetector",
        help="Registered model name",
    )

    args = parser.parse_args()

    if args.rollback:
        rollback_model(args.model_name)
        print(f"✅ Rolled back {args.model_name} to previous version")
    elif args.stage:
        stage = "Staging" if args.stage == "staging" else "Production"
        promote_model(args.model_name, version=args.version, stage=stage)
        print(f"✅ Promoted {args.model_name} to {stage}")
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
