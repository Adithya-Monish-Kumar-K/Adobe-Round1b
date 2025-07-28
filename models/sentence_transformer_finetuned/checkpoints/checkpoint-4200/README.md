---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:801
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: '{''role'': ''HR professional''}: {''task'': ''Create and manage
    fillable forms for onboarding and compliance.''}'
  sentences:
  - Generate Images
  - 1.   From the Quick action toolbar, select  Add your signature or initials
  - Before you begin, ensure that you adhere to the file and usage-related restrictions
    and login  requirements.
- source_sentence: '{''role'': ''HR professional''}: {''task'': ''Create and manage
    fillable forms for onboarding and compliance.''}'
  sentences:
  - Add or edit lists
  - 'Ingredients:'
  - 3.   Click an action to from the button menu, and follow the onscreen prompts
    to save  the files.  4.   The PDF opens in Acrobat. Click Start in the right-hand
    pane to process the file.   Click an action to from the button menu, and follow
    the onscreen prompts to save
- source_sentence: '{''role'': ''Food Contractor''}: {''task'': ''Prepare a vegetarian
    buffet-style dinner menu for a corporate gathering, including gluten-free items.''}'
  sentences:
  - '   1 teaspoon thyme     1 teaspoon rosemary     1/4 cup olive oil     Salt
    and pepper to taste  '
  - 'Chicken Salad Lettuce Wraps  Ingredients:'
  - 1.   Open Acrobat and then open a document. Select AI Assistant. Select the add  button   from
    the lower left. It opens the Select files to use with AI Assistant. Select the  files
    you want to add and select Next from the upper right.   Open Acrobat and then
    open a document. Select AI Assistant. Select the add
- source_sentence: '{''role'': ''Travel Planner''}: {''task'': ''Plan a trip of 4
    days for a group of 10 college friends.''}'
  sentences:
  - Pottery and Ceramics
  - Acrobat desktop
  - 'There are two methods to apply fields:'
- source_sentence: '{''role'': ''HR professional''}: {''task'': ''Create and manage
    fillable forms for onboarding and compliance.''}'
  sentences:
  - 'The Ultimate South of France Travel Companion: Your Comprehensive Guide to Packing,  Planning,
    and Exploring'
  - If you want to use the same settings every time you convert PDFs to a particular
    format,  specify those settings in the  Preferences  dialog box. In the  Convert
    From PDF  panel, select a  file format from the list and select  Edit Settings
    . You can select the  Defaults  at the top of  the  Save as Settings  dialog box
    to revert to the default settings.
  - If you're an admin, you can purchase an AI Assistant for Acrobat add-on subscription
    through  the Admin Console if your team members have consumed the free requests
    or require more  licenses.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: sts dev
      type: sts-dev
    metrics:
    - type: pearson_cosine
      value: 0.9995660460329715
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.18257573994228216
      name: Spearman Cosine
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    "{'role': 'HR professional'}: {'task': 'Create and manage fillable forms for onboarding and compliance.'}",
    "If you're an admin, you can purchase an AI Assistant for Acrobat add-on subscription through  the Admin Console if your team members have consumed the free requests or require more  licenses.",
    'The Ultimate South of France Travel Companion: Your Comprehensive Guide to Packing,  Planning, and Exploring',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.0065, 0.0072],
#         [0.0065, 1.0000, 0.7646],
#         [0.0072, 0.7646, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Semantic Similarity

* Dataset: `sts-dev`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.9996     |
| **spearman_cosine** | **0.1826** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 801 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 801 samples:
  |         | sentence_0                                                                         | sentence_1                                                                         | label                                                          |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             | float                                                          |
  | details | <ul><li>min: 33 tokens</li><li>mean: 34.04 tokens</li><li>max: 42 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 18.49 tokens</li><li>max: 109 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.01</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                            | sentence_1                             | label            |
  |:----------------------------------------------------------------------------------------------------------------------|:---------------------------------------|:-----------------|
  | <code>{'role': 'HR professional'}: {'task': 'Create and manage fillable forms for onboarding and compliance.'}</code> | <code>document?</code>                 | <code>0.0</code> |
  | <code>{'role': 'HR professional'}: {'task': 'Create and manage fillable forms for onboarding and compliance.'}</code> | <code>Request access in Acrobat</code> | <code>0.0</code> |
  | <code>{'role': 'HR professional'}: {'task': 'Create and manage fillable forms for onboarding and compliance.'}</code> | <code>Conversion</code>                | <code>0.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `num_train_epochs`: 500
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 500
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch   | Step | Training Loss | sts-dev_spearman_cosine |
|:-------:|:----:|:-------------:|:-----------------------:|
| 0.1961  | 10   | -             | 0.0830                  |
| 0.3922  | 20   | -             | 0.0954                  |
| 0.5882  | 30   | -             | 0.0996                  |
| 0.7843  | 40   | -             | 0.1037                  |
| 0.9804  | 50   | -             | 0.1411                  |
| 1.0     | 51   | -             | 0.1411                  |
| 1.1765  | 60   | -             | 0.1494                  |
| 1.3725  | 70   | -             | 0.1784                  |
| 1.5686  | 80   | -             | 0.1784                  |
| 1.7647  | 90   | -             | 0.1784                  |
| 1.9608  | 100  | -             | 0.1701                  |
| 2.0     | 102  | -             | 0.1701                  |
| 2.1569  | 110  | -             | 0.1701                  |
| 2.3529  | 120  | -             | 0.1618                  |
| 2.5490  | 130  | -             | 0.1328                  |
| 2.7451  | 140  | -             | 0.1784                  |
| 2.9412  | 150  | -             | 0.1826                  |
| 3.0     | 153  | -             | 0.1826                  |
| 3.1373  | 160  | -             | 0.1784                  |
| 3.3333  | 170  | -             | 0.1743                  |
| 3.5294  | 180  | -             | 0.1826                  |
| 3.7255  | 190  | -             | 0.1826                  |
| 3.9216  | 200  | -             | 0.1826                  |
| 4.0     | 204  | -             | 0.1826                  |
| 4.1176  | 210  | -             | 0.1826                  |
| 4.3137  | 220  | -             | 0.1784                  |
| 4.5098  | 230  | -             | 0.1784                  |
| 4.7059  | 240  | -             | 0.1784                  |
| 4.9020  | 250  | -             | 0.1826                  |
| 5.0     | 255  | -             | 0.1826                  |
| 5.0980  | 260  | -             | 0.1826                  |
| 5.2941  | 270  | -             | 0.1826                  |
| 5.4902  | 280  | -             | 0.1826                  |
| 5.6863  | 290  | -             | 0.1826                  |
| 5.8824  | 300  | -             | 0.1826                  |
| 6.0     | 306  | -             | 0.1826                  |
| 6.0784  | 310  | -             | 0.1826                  |
| 6.2745  | 320  | -             | 0.1826                  |
| 6.4706  | 330  | -             | 0.1826                  |
| 6.6667  | 340  | -             | 0.1826                  |
| 6.8627  | 350  | -             | 0.1826                  |
| 7.0     | 357  | -             | 0.1826                  |
| 7.0588  | 360  | -             | 0.1826                  |
| 7.2549  | 370  | -             | 0.1826                  |
| 7.4510  | 380  | -             | 0.1826                  |
| 7.6471  | 390  | -             | 0.1826                  |
| 7.8431  | 400  | -             | 0.1826                  |
| 8.0     | 408  | -             | 0.1826                  |
| 8.0392  | 410  | -             | 0.1826                  |
| 8.2353  | 420  | -             | 0.1826                  |
| 8.4314  | 430  | -             | 0.1826                  |
| 8.6275  | 440  | -             | 0.1826                  |
| 8.8235  | 450  | -             | 0.1826                  |
| 9.0     | 459  | -             | 0.1826                  |
| 9.0196  | 460  | -             | 0.1826                  |
| 9.2157  | 470  | -             | 0.1826                  |
| 9.4118  | 480  | -             | 0.1826                  |
| 9.6078  | 490  | -             | 0.1826                  |
| 9.8039  | 500  | 0.0079        | 0.1826                  |
| 10.0    | 510  | -             | 0.1826                  |
| 10.1961 | 520  | -             | 0.1826                  |
| 10.3922 | 530  | -             | 0.1826                  |
| 10.5882 | 540  | -             | 0.1826                  |
| 10.7843 | 550  | -             | 0.1826                  |
| 10.9804 | 560  | -             | 0.1826                  |
| 11.0    | 561  | -             | 0.1826                  |
| 11.1765 | 570  | -             | 0.1826                  |
| 11.3725 | 580  | -             | 0.1826                  |
| 11.5686 | 590  | -             | 0.1826                  |
| 11.7647 | 600  | -             | 0.1826                  |
| 11.9608 | 610  | -             | 0.1826                  |
| 12.0    | 612  | -             | 0.1826                  |
| 12.1569 | 620  | -             | 0.1826                  |
| 12.3529 | 630  | -             | 0.1826                  |
| 12.5490 | 640  | -             | 0.1826                  |
| 12.7451 | 650  | -             | 0.1826                  |
| 12.9412 | 660  | -             | 0.1826                  |
| 13.0    | 663  | -             | 0.1826                  |
| 13.1373 | 670  | -             | 0.1826                  |
| 13.3333 | 680  | -             | 0.1826                  |
| 13.5294 | 690  | -             | 0.1826                  |
| 13.7255 | 700  | -             | 0.1826                  |
| 13.9216 | 710  | -             | 0.1826                  |
| 14.0    | 714  | -             | 0.1826                  |
| 14.1176 | 720  | -             | 0.1826                  |
| 14.3137 | 730  | -             | 0.1826                  |
| 14.5098 | 740  | -             | 0.1826                  |
| 14.7059 | 750  | -             | 0.1826                  |
| 14.9020 | 760  | -             | 0.1826                  |
| 15.0    | 765  | -             | 0.1826                  |
| 15.0980 | 770  | -             | 0.1826                  |
| 15.2941 | 780  | -             | 0.1826                  |
| 15.4902 | 790  | -             | 0.1826                  |
| 15.6863 | 800  | -             | 0.1826                  |
| 15.8824 | 810  | -             | 0.1826                  |
| 16.0    | 816  | -             | 0.1826                  |
| 16.0784 | 820  | -             | 0.1826                  |
| 16.2745 | 830  | -             | 0.1826                  |
| 16.4706 | 840  | -             | 0.1826                  |
| 16.6667 | 850  | -             | 0.1826                  |
| 16.8627 | 860  | -             | 0.1826                  |
| 17.0    | 867  | -             | 0.1826                  |
| 17.0588 | 870  | -             | 0.1826                  |
| 17.2549 | 880  | -             | 0.1826                  |
| 17.4510 | 890  | -             | 0.1826                  |
| 17.6471 | 900  | -             | 0.1826                  |
| 17.8431 | 910  | -             | 0.1826                  |
| 18.0    | 918  | -             | 0.1826                  |
| 18.0392 | 920  | -             | 0.1826                  |
| 18.2353 | 930  | -             | 0.1826                  |
| 18.4314 | 940  | -             | 0.1826                  |
| 18.6275 | 950  | -             | 0.1826                  |
| 18.8235 | 960  | -             | 0.1826                  |
| 19.0    | 969  | -             | 0.1826                  |
| 19.0196 | 970  | -             | 0.1826                  |
| 19.2157 | 980  | -             | 0.1826                  |
| 19.4118 | 990  | -             | 0.1826                  |
| 19.6078 | 1000 | 0.0015        | 0.1826                  |
| 19.8039 | 1010 | -             | 0.1826                  |
| 20.0    | 1020 | -             | 0.1826                  |
| 20.1961 | 1030 | -             | 0.1826                  |
| 20.3922 | 1040 | -             | 0.1826                  |
| 20.5882 | 1050 | -             | 0.1826                  |
| 20.7843 | 1060 | -             | 0.1826                  |
| 20.9804 | 1070 | -             | 0.1826                  |
| 21.0    | 1071 | -             | 0.1826                  |
| 21.1765 | 1080 | -             | 0.1826                  |
| 21.3725 | 1090 | -             | 0.1826                  |
| 21.5686 | 1100 | -             | 0.1826                  |
| 21.7647 | 1110 | -             | 0.1826                  |
| 21.9608 | 1120 | -             | 0.1826                  |
| 22.0    | 1122 | -             | 0.1826                  |
| 22.1569 | 1130 | -             | 0.1826                  |
| 22.3529 | 1140 | -             | 0.1826                  |
| 22.5490 | 1150 | -             | 0.1826                  |
| 22.7451 | 1160 | -             | 0.1826                  |
| 22.9412 | 1170 | -             | 0.1826                  |
| 23.0    | 1173 | -             | 0.1826                  |
| 23.1373 | 1180 | -             | 0.1826                  |
| 23.3333 | 1190 | -             | 0.1826                  |
| 23.5294 | 1200 | -             | 0.1826                  |
| 23.7255 | 1210 | -             | 0.1826                  |
| 23.9216 | 1220 | -             | 0.1826                  |
| 24.0    | 1224 | -             | 0.1826                  |
| 24.1176 | 1230 | -             | 0.1826                  |
| 24.3137 | 1240 | -             | 0.1826                  |
| 24.5098 | 1250 | -             | 0.1826                  |
| 24.7059 | 1260 | -             | 0.1826                  |
| 24.9020 | 1270 | -             | 0.1826                  |
| 25.0    | 1275 | -             | 0.1826                  |
| 25.0980 | 1280 | -             | 0.1826                  |
| 25.2941 | 1290 | -             | 0.1826                  |
| 25.4902 | 1300 | -             | 0.1826                  |
| 25.6863 | 1310 | -             | 0.1826                  |
| 25.8824 | 1320 | -             | 0.1826                  |
| 26.0    | 1326 | -             | 0.1826                  |
| 26.0784 | 1330 | -             | 0.1826                  |
| 26.2745 | 1340 | -             | 0.1826                  |
| 26.4706 | 1350 | -             | 0.1826                  |
| 26.6667 | 1360 | -             | 0.1826                  |
| 26.8627 | 1370 | -             | 0.1826                  |
| 27.0    | 1377 | -             | 0.1826                  |
| 27.0588 | 1380 | -             | 0.1826                  |
| 27.2549 | 1390 | -             | 0.1826                  |
| 27.4510 | 1400 | -             | 0.1826                  |
| 27.6471 | 1410 | -             | 0.1826                  |
| 27.8431 | 1420 | -             | 0.1826                  |
| 28.0    | 1428 | -             | 0.1826                  |
| 28.0392 | 1430 | -             | 0.1826                  |
| 28.2353 | 1440 | -             | 0.1826                  |
| 28.4314 | 1450 | -             | 0.1826                  |
| 28.6275 | 1460 | -             | 0.1826                  |
| 28.8235 | 1470 | -             | 0.1826                  |
| 29.0    | 1479 | -             | 0.1826                  |
| 29.0196 | 1480 | -             | 0.1826                  |
| 29.2157 | 1490 | -             | 0.1826                  |
| 29.4118 | 1500 | 0.0005        | 0.1826                  |
| 29.6078 | 1510 | -             | 0.1826                  |
| 29.8039 | 1520 | -             | 0.1826                  |
| 30.0    | 1530 | -             | 0.1826                  |
| 30.1961 | 1540 | -             | 0.1826                  |
| 30.3922 | 1550 | -             | 0.1826                  |
| 30.5882 | 1560 | -             | 0.1826                  |
| 30.7843 | 1570 | -             | 0.1826                  |
| 30.9804 | 1580 | -             | 0.1826                  |
| 31.0    | 1581 | -             | 0.1826                  |
| 31.1765 | 1590 | -             | 0.1826                  |
| 31.3725 | 1600 | -             | 0.1826                  |
| 31.5686 | 1610 | -             | 0.1826                  |
| 31.7647 | 1620 | -             | 0.1826                  |
| 31.9608 | 1630 | -             | 0.1826                  |
| 32.0    | 1632 | -             | 0.1826                  |
| 32.1569 | 1640 | -             | 0.1826                  |
| 32.3529 | 1650 | -             | 0.1826                  |
| 32.5490 | 1660 | -             | 0.1826                  |
| 32.7451 | 1670 | -             | 0.1826                  |
| 32.9412 | 1680 | -             | 0.1826                  |
| 33.0    | 1683 | -             | 0.1826                  |
| 33.1373 | 1690 | -             | 0.1826                  |
| 33.3333 | 1700 | -             | 0.1826                  |
| 33.5294 | 1710 | -             | 0.1826                  |
| 33.7255 | 1720 | -             | 0.1826                  |
| 33.9216 | 1730 | -             | 0.1826                  |
| 34.0    | 1734 | -             | 0.1826                  |
| 34.1176 | 1740 | -             | 0.1826                  |
| 34.3137 | 1750 | -             | 0.1826                  |
| 34.5098 | 1760 | -             | 0.1826                  |
| 34.7059 | 1770 | -             | 0.1826                  |
| 34.9020 | 1780 | -             | 0.1826                  |
| 35.0    | 1785 | -             | 0.1826                  |
| 35.0980 | 1790 | -             | 0.1826                  |
| 35.2941 | 1800 | -             | 0.1826                  |
| 35.4902 | 1810 | -             | 0.1826                  |
| 35.6863 | 1820 | -             | 0.1826                  |
| 35.8824 | 1830 | -             | 0.1826                  |
| 36.0    | 1836 | -             | 0.1826                  |
| 36.0784 | 1840 | -             | 0.1826                  |
| 36.2745 | 1850 | -             | 0.1826                  |
| 36.4706 | 1860 | -             | 0.1826                  |
| 36.6667 | 1870 | -             | 0.1826                  |
| 36.8627 | 1880 | -             | 0.1826                  |
| 37.0    | 1887 | -             | 0.1826                  |
| 37.0588 | 1890 | -             | 0.1826                  |
| 37.2549 | 1900 | -             | 0.1826                  |
| 37.4510 | 1910 | -             | 0.1826                  |
| 37.6471 | 1920 | -             | 0.1826                  |
| 37.8431 | 1930 | -             | 0.1826                  |
| 38.0    | 1938 | -             | 0.1826                  |
| 38.0392 | 1940 | -             | 0.1826                  |
| 38.2353 | 1950 | -             | 0.1826                  |
| 38.4314 | 1960 | -             | 0.1826                  |
| 38.6275 | 1970 | -             | 0.1826                  |
| 38.8235 | 1980 | -             | 0.1826                  |
| 39.0    | 1989 | -             | 0.1826                  |
| 39.0196 | 1990 | -             | 0.1826                  |
| 39.2157 | 2000 | 0.0003        | 0.1826                  |
| 39.4118 | 2010 | -             | 0.1826                  |
| 39.6078 | 2020 | -             | 0.1826                  |
| 39.8039 | 2030 | -             | 0.1826                  |
| 40.0    | 2040 | -             | 0.1826                  |
| 40.1961 | 2050 | -             | 0.1826                  |
| 40.3922 | 2060 | -             | 0.1826                  |
| 40.5882 | 2070 | -             | 0.1826                  |
| 40.7843 | 2080 | -             | 0.1826                  |
| 40.9804 | 2090 | -             | 0.1826                  |
| 41.0    | 2091 | -             | 0.1826                  |
| 41.1765 | 2100 | -             | 0.1826                  |
| 41.3725 | 2110 | -             | 0.1826                  |
| 41.5686 | 2120 | -             | 0.1826                  |
| 41.7647 | 2130 | -             | 0.1826                  |
| 41.9608 | 2140 | -             | 0.1826                  |
| 42.0    | 2142 | -             | 0.1826                  |
| 42.1569 | 2150 | -             | 0.1826                  |
| 42.3529 | 2160 | -             | 0.1826                  |
| 42.5490 | 2170 | -             | 0.1826                  |
| 42.7451 | 2180 | -             | 0.1826                  |
| 42.9412 | 2190 | -             | 0.1826                  |
| 43.0    | 2193 | -             | 0.1826                  |
| 43.1373 | 2200 | -             | 0.1826                  |
| 43.3333 | 2210 | -             | 0.1826                  |
| 43.5294 | 2220 | -             | 0.1826                  |
| 43.7255 | 2230 | -             | 0.1826                  |
| 43.9216 | 2240 | -             | 0.1826                  |
| 44.0    | 2244 | -             | 0.1826                  |
| 44.1176 | 2250 | -             | 0.1826                  |
| 44.3137 | 2260 | -             | 0.1826                  |
| 44.5098 | 2270 | -             | 0.1826                  |
| 44.7059 | 2280 | -             | 0.1826                  |
| 44.9020 | 2290 | -             | 0.1826                  |
| 45.0    | 2295 | -             | 0.1826                  |
| 45.0980 | 2300 | -             | 0.1826                  |
| 45.2941 | 2310 | -             | 0.1826                  |
| 45.4902 | 2320 | -             | 0.1826                  |
| 45.6863 | 2330 | -             | 0.1826                  |
| 45.8824 | 2340 | -             | 0.1826                  |
| 46.0    | 2346 | -             | 0.1826                  |
| 46.0784 | 2350 | -             | 0.1826                  |
| 46.2745 | 2360 | -             | 0.1826                  |
| 46.4706 | 2370 | -             | 0.1826                  |
| 46.6667 | 2380 | -             | 0.1826                  |
| 46.8627 | 2390 | -             | 0.1826                  |
| 47.0    | 2397 | -             | 0.1826                  |
| 47.0588 | 2400 | -             | 0.1826                  |
| 47.2549 | 2410 | -             | 0.1826                  |
| 47.4510 | 2420 | -             | 0.1826                  |
| 47.6471 | 2430 | -             | 0.1826                  |
| 47.8431 | 2440 | -             | 0.1826                  |
| 48.0    | 2448 | -             | 0.1826                  |
| 48.0392 | 2450 | -             | 0.1826                  |
| 48.2353 | 2460 | -             | 0.1826                  |
| 48.4314 | 2470 | -             | 0.1826                  |
| 48.6275 | 2480 | -             | 0.1826                  |
| 48.8235 | 2490 | -             | 0.1826                  |
| 49.0    | 2499 | -             | 0.1826                  |
| 49.0196 | 2500 | 0.0001        | 0.1826                  |
| 49.2157 | 2510 | -             | 0.1826                  |
| 49.4118 | 2520 | -             | 0.1826                  |
| 49.6078 | 2530 | -             | 0.1826                  |
| 49.8039 | 2540 | -             | 0.1826                  |
| 50.0    | 2550 | -             | 0.1826                  |
| 50.1961 | 2560 | -             | 0.1826                  |
| 50.3922 | 2570 | -             | 0.1826                  |
| 50.5882 | 2580 | -             | 0.1826                  |
| 50.7843 | 2590 | -             | 0.1826                  |
| 50.9804 | 2600 | -             | 0.1826                  |
| 51.0    | 2601 | -             | 0.1826                  |
| 51.1765 | 2610 | -             | 0.1826                  |
| 51.3725 | 2620 | -             | 0.1826                  |
| 51.5686 | 2630 | -             | 0.1826                  |
| 51.7647 | 2640 | -             | 0.1826                  |
| 51.9608 | 2650 | -             | 0.1826                  |
| 52.0    | 2652 | -             | 0.1826                  |
| 52.1569 | 2660 | -             | 0.1826                  |
| 52.3529 | 2670 | -             | 0.1826                  |
| 52.5490 | 2680 | -             | 0.1826                  |
| 52.7451 | 2690 | -             | 0.1826                  |
| 52.9412 | 2700 | -             | 0.1826                  |
| 53.0    | 2703 | -             | 0.1826                  |
| 53.1373 | 2710 | -             | 0.1826                  |
| 53.3333 | 2720 | -             | 0.1826                  |
| 53.5294 | 2730 | -             | 0.1826                  |
| 53.7255 | 2740 | -             | 0.1826                  |
| 53.9216 | 2750 | -             | 0.1826                  |
| 54.0    | 2754 | -             | 0.1826                  |
| 54.1176 | 2760 | -             | 0.1826                  |
| 54.3137 | 2770 | -             | 0.1826                  |
| 54.5098 | 2780 | -             | 0.1826                  |
| 54.7059 | 2790 | -             | 0.1826                  |
| 54.9020 | 2800 | -             | 0.1826                  |
| 55.0    | 2805 | -             | 0.1826                  |
| 55.0980 | 2810 | -             | 0.1826                  |
| 55.2941 | 2820 | -             | 0.1826                  |
| 55.4902 | 2830 | -             | 0.1826                  |
| 55.6863 | 2840 | -             | 0.1826                  |
| 55.8824 | 2850 | -             | 0.1826                  |
| 56.0    | 2856 | -             | 0.1826                  |
| 56.0784 | 2860 | -             | 0.1826                  |
| 56.2745 | 2870 | -             | 0.1826                  |
| 56.4706 | 2880 | -             | 0.1826                  |
| 56.6667 | 2890 | -             | 0.1826                  |
| 56.8627 | 2900 | -             | 0.1826                  |
| 57.0    | 2907 | -             | 0.1826                  |
| 57.0588 | 2910 | -             | 0.1826                  |
| 57.2549 | 2920 | -             | 0.1826                  |
| 57.4510 | 2930 | -             | 0.1826                  |
| 57.6471 | 2940 | -             | 0.1826                  |
| 57.8431 | 2950 | -             | 0.1826                  |
| 58.0    | 2958 | -             | 0.1826                  |
| 58.0392 | 2960 | -             | 0.1826                  |
| 58.2353 | 2970 | -             | 0.1826                  |
| 58.4314 | 2980 | -             | 0.1826                  |
| 58.6275 | 2990 | -             | 0.1826                  |
| 58.8235 | 3000 | 0.0001        | 0.1826                  |
| 59.0    | 3009 | -             | 0.1826                  |
| 59.0196 | 3010 | -             | 0.1826                  |
| 59.2157 | 3020 | -             | 0.1826                  |
| 59.4118 | 3030 | -             | 0.1826                  |
| 59.6078 | 3040 | -             | 0.1826                  |
| 59.8039 | 3050 | -             | 0.1826                  |
| 60.0    | 3060 | -             | 0.1826                  |
| 60.1961 | 3070 | -             | 0.1826                  |
| 60.3922 | 3080 | -             | 0.1826                  |
| 60.5882 | 3090 | -             | 0.1826                  |
| 60.7843 | 3100 | -             | 0.1826                  |
| 60.9804 | 3110 | -             | 0.1826                  |
| 61.0    | 3111 | -             | 0.1826                  |
| 61.1765 | 3120 | -             | 0.1826                  |
| 61.3725 | 3130 | -             | 0.1826                  |
| 61.5686 | 3140 | -             | 0.1826                  |
| 61.7647 | 3150 | -             | 0.1826                  |
| 61.9608 | 3160 | -             | 0.1826                  |
| 62.0    | 3162 | -             | 0.1826                  |
| 62.1569 | 3170 | -             | 0.1826                  |
| 62.3529 | 3180 | -             | 0.1826                  |
| 62.5490 | 3190 | -             | 0.1826                  |
| 62.7451 | 3200 | -             | 0.1826                  |
| 62.9412 | 3210 | -             | 0.1826                  |
| 63.0    | 3213 | -             | 0.1826                  |
| 63.1373 | 3220 | -             | 0.1826                  |
| 63.3333 | 3230 | -             | 0.1826                  |
| 63.5294 | 3240 | -             | 0.1826                  |
| 63.7255 | 3250 | -             | 0.1826                  |
| 63.9216 | 3260 | -             | 0.1826                  |
| 64.0    | 3264 | -             | 0.1826                  |
| 64.1176 | 3270 | -             | 0.1826                  |
| 64.3137 | 3280 | -             | 0.1826                  |
| 64.5098 | 3290 | -             | 0.1826                  |
| 64.7059 | 3300 | -             | 0.1826                  |
| 64.9020 | 3310 | -             | 0.1826                  |
| 65.0    | 3315 | -             | 0.1826                  |
| 65.0980 | 3320 | -             | 0.1826                  |
| 65.2941 | 3330 | -             | 0.1826                  |
| 65.4902 | 3340 | -             | 0.1826                  |
| 65.6863 | 3350 | -             | 0.1826                  |
| 65.8824 | 3360 | -             | 0.1826                  |
| 66.0    | 3366 | -             | 0.1826                  |
| 66.0784 | 3370 | -             | 0.1826                  |
| 66.2745 | 3380 | -             | 0.1826                  |
| 66.4706 | 3390 | -             | 0.1826                  |
| 66.6667 | 3400 | -             | 0.1826                  |
| 66.8627 | 3410 | -             | 0.1826                  |
| 67.0    | 3417 | -             | 0.1826                  |
| 67.0588 | 3420 | -             | 0.1826                  |
| 67.2549 | 3430 | -             | 0.1826                  |
| 67.4510 | 3440 | -             | 0.1826                  |
| 67.6471 | 3450 | -             | 0.1826                  |
| 67.8431 | 3460 | -             | 0.1826                  |
| 68.0    | 3468 | -             | 0.1826                  |
| 68.0392 | 3470 | -             | 0.1826                  |
| 68.2353 | 3480 | -             | 0.1826                  |
| 68.4314 | 3490 | -             | 0.1826                  |
| 68.6275 | 3500 | 0.0001        | 0.1826                  |
| 68.8235 | 3510 | -             | 0.1826                  |
| 69.0    | 3519 | -             | 0.1826                  |
| 69.0196 | 3520 | -             | 0.1826                  |
| 69.2157 | 3530 | -             | 0.1826                  |
| 69.4118 | 3540 | -             | 0.1826                  |
| 69.6078 | 3550 | -             | 0.1826                  |
| 69.8039 | 3560 | -             | 0.1826                  |
| 70.0    | 3570 | -             | 0.1826                  |
| 70.1961 | 3580 | -             | 0.1826                  |
| 70.3922 | 3590 | -             | 0.1826                  |
| 70.5882 | 3600 | -             | 0.1826                  |
| 70.7843 | 3610 | -             | 0.1826                  |
| 70.9804 | 3620 | -             | 0.1826                  |
| 71.0    | 3621 | -             | 0.1826                  |
| 71.1765 | 3630 | -             | 0.1826                  |
| 71.3725 | 3640 | -             | 0.1826                  |
| 71.5686 | 3650 | -             | 0.1826                  |
| 71.7647 | 3660 | -             | 0.1826                  |
| 71.9608 | 3670 | -             | 0.1826                  |
| 72.0    | 3672 | -             | 0.1826                  |
| 72.1569 | 3680 | -             | 0.1826                  |
| 72.3529 | 3690 | -             | 0.1826                  |
| 72.5490 | 3700 | -             | 0.1826                  |
| 72.7451 | 3710 | -             | 0.1826                  |
| 72.9412 | 3720 | -             | 0.1826                  |
| 73.0    | 3723 | -             | 0.1826                  |
| 73.1373 | 3730 | -             | 0.1826                  |
| 73.3333 | 3740 | -             | 0.1826                  |
| 73.5294 | 3750 | -             | 0.1826                  |
| 73.7255 | 3760 | -             | 0.1826                  |
| 73.9216 | 3770 | -             | 0.1826                  |
| 74.0    | 3774 | -             | 0.1826                  |
| 74.1176 | 3780 | -             | 0.1826                  |
| 74.3137 | 3790 | -             | 0.1826                  |
| 74.5098 | 3800 | -             | 0.1826                  |
| 74.7059 | 3810 | -             | 0.1826                  |
| 74.9020 | 3820 | -             | 0.1826                  |
| 75.0    | 3825 | -             | 0.1826                  |
| 75.0980 | 3830 | -             | 0.1826                  |
| 75.2941 | 3840 | -             | 0.1826                  |
| 75.4902 | 3850 | -             | 0.1826                  |
| 75.6863 | 3860 | -             | 0.1826                  |
| 75.8824 | 3870 | -             | 0.1826                  |
| 76.0    | 3876 | -             | 0.1826                  |
| 76.0784 | 3880 | -             | 0.1826                  |
| 76.2745 | 3890 | -             | 0.1826                  |
| 76.4706 | 3900 | -             | 0.1826                  |
| 76.6667 | 3910 | -             | 0.1826                  |
| 76.8627 | 3920 | -             | 0.1826                  |
| 77.0    | 3927 | -             | 0.1826                  |
| 77.0588 | 3930 | -             | 0.1826                  |
| 77.2549 | 3940 | -             | 0.1826                  |
| 77.4510 | 3950 | -             | 0.1826                  |
| 77.6471 | 3960 | -             | 0.1826                  |
| 77.8431 | 3970 | -             | 0.1826                  |
| 78.0    | 3978 | -             | 0.1826                  |
| 78.0392 | 3980 | -             | 0.1826                  |
| 78.2353 | 3990 | -             | 0.1826                  |
| 78.4314 | 4000 | 0.0           | 0.1826                  |
| 78.6275 | 4010 | -             | 0.1826                  |
| 78.8235 | 4020 | -             | 0.1826                  |
| 79.0    | 4029 | -             | 0.1826                  |
| 79.0196 | 4030 | -             | 0.1826                  |
| 79.2157 | 4040 | -             | 0.1826                  |
| 79.4118 | 4050 | -             | 0.1826                  |
| 79.6078 | 4060 | -             | 0.1826                  |
| 79.8039 | 4070 | -             | 0.1826                  |
| 80.0    | 4080 | -             | 0.1826                  |
| 80.1961 | 4090 | -             | 0.1826                  |
| 80.3922 | 4100 | -             | 0.1826                  |
| 80.5882 | 4110 | -             | 0.1826                  |
| 80.7843 | 4120 | -             | 0.1826                  |
| 80.9804 | 4130 | -             | 0.1826                  |
| 81.0    | 4131 | -             | 0.1826                  |
| 81.1765 | 4140 | -             | 0.1826                  |
| 81.3725 | 4150 | -             | 0.1826                  |
| 81.5686 | 4160 | -             | 0.1826                  |
| 81.7647 | 4170 | -             | 0.1826                  |
| 81.9608 | 4180 | -             | 0.1826                  |
| 82.0    | 4182 | -             | 0.1826                  |
| 82.1569 | 4190 | -             | 0.1826                  |
| 82.3529 | 4200 | -             | 0.1826                  |

</details>

### Framework Versions
- Python: 3.13.5
- Sentence Transformers: 5.0.0
- Transformers: 4.54.0
- PyTorch: 2.7.1+cu128
- Accelerate: 1.9.0
- Datasets: 4.0.0
- Tokenizers: 0.21.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->