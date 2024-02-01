"""
DPO strategies for WizardCoder
"""


def argilla(
    cfg,
):  # pylint: disable=possibly-unused-variable,unused-argument
    def transform_fn(sample):
        sample["prompt"] = f"Below is an instruction that describes a task. " \
                           f"Write a response that appropriately completes the request.\n\n" \
                           f"### Instruction:\n{sample['instruction']}\n\n### Response:\n"
        sample["chosen"] = f"{sample['chosen_response']}<|endoftext|>"
        sample["rejected"] = f"{sample['rejected_response']}<|endoftext|>"
        return sample

    return transform_fn


def intel(cfg):  # pylint: disable=possibly-unused-variable,unused-argument
    """
    For Intel Orca DPO Pairs
    """

    def transform_fn(sample):
        sample["prompt"] = f"Below is an instruction that describes a task. " \
                           f"Write a response that appropriately completes the request.\n\n" \
                           f"### Instruction:\n{sample['instruction']}\n\n### Response:\n"
        sample["chosen"] = f"{sample['chosen']}<|endoftext|>"
        sample["rejected"] = f"{sample['rejected']}<|endoftext|>"
        return sample

    return transform_fn
