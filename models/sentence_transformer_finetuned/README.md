---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:209
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: 'Travel Planner: Plan a trip of 4 days for a group of 10 college
    friends.'
  sentences:
  - 'General Packing Tips and Tricks: Layering - The weather can vary, so pack layers
    to stay comfortable in different temperatures; Versatile Clothing - Choose items
    that can be mixed and matched to create multiple outfits, helping you pack lighter;
    Packing Cubes - Use packing cubes to organize your clothes and maximize suitcase
    space; Roll Your Clothes - Rolling clothes saves space and reduces wrinkles; Travel-Sized
    Toiletries - Bring travel-sized toiletries to save space and comply with airline
    regulations; Reusable Bags - Pack a few reusable bags for laundry, shoes, or shopping;
    First Aid Kit - Include a small first aid kit with band-aids, antiseptic wipes,
    and any necessary medications; Copies of Important Documents - Make copies of
    your passport, travel insurance, and other important documents. Keep them separate
    from the originals.'
  - 'Nice: The Jewel of the French Riviera'
  - 'You can create PDFs from text and images that you copy from applications on macOS
    or Windows. 1. Capture content in the Clipboard:  Use the copy command in the
    applications.  Press the PrintScreen key (Windows).  Use the Screenshot utility
    (Applications  Utilities  Screenshot), and choose Edit  Copy'
- source_sentence: Help me Create and manage fillable forms for onboarding and compliance.
  sentences:
  - 'You can create multiple PDFs from multiple native files, including files of different
    supported formats, in one operation. This method is useful when you must convert
    a large number of files to PDF. Note: When you use this method, Acrobat applies
    the most recently used conversion settings without of'
  - Convert clipboard content to PDF
  - 'The South of France offers a vibrant nightlife scene, with options ranging from
    chic bars to lively nightclubs: Bars and Lounges - Monaco: Enjoy classic cocktails
    and live jazz at Le Bar Americain, located in the Hôtel de Paris; Nice: Try creative
    cocktails at Le Comptoir du Marché, a trendy bar in the old town; Cannes: Experience
    dining and entertainment at La Folie Douce, with live music, DJs, and performances;
    Marseille: Visit Le Trolleybus, a popular bar with multiple rooms and music styles;
    Saint-Tropez: Relax at Bar du Port, known for its chic atmosphere and waterfront
    views. Nightclubs - Saint-Tropez: Dance at the famous Les Caves du Roy, known
    for its glamorous atmosphere and celebrity clientele; Nice: Party at High Club
    on the Promenade des Anglais, featuring multiple dance floors and top DJs; Cannes:
    Enjoy the stylish setting and rooftop terrace at La Suite, offering stunning views
    of Cannes.'
- source_sentence: Create and manage fillable forms for onboarding and compliance.
  sentences:
  - Conversion
  - Introduction The South of France, known for its stunning landscapes, Mediterranean
    coastline, and rich cultural heritage, is home to some of the most beautiful and
    historically significant cities in the country. This guide provides an in-depth
    look at the major cities in the South of France, detaili
  - The Course Camarguaise is a traditional bullfighting sport unique to the Camargue
    region. Unlike Spanish bullfighting, the objective is not to harm the bull but
    to remove ribbons and other decorations
- source_sentence: 'HR professional: Create and manage fillable forms for onboarding
    and compliance.'
  sentences:
  - Keep an annotation tool selected
  - Culinary Experiences
  - 'General Packing Tips and Tricks: Layering: The weather can vary, so pack layers
    to stay comfortable in diﬀerent temperatures.  Versatile Clothing: Choose items
    that can be mixed and matched to create multiple outfits, helping you pac'
- source_sentence: Plan a trip of 4 days for a group of 10 college friends.
  sentences:
  - Culinary Experiences
  - 'Water Sports: Cannes, Nice, and Saint-Tropez - Try jet skiing or parasailing
    for a thrill; Toulon - Dive into the underwater world with scuba diving excursions
    to explore wrecks; Cerbère-Banyuls - Visit the marine reserve for an unforgettable
    diving experience; Mediterranean Coast - Charter a yacht or join a sailing tour
    to explore the coastline and nearby islands; Marseille - Go windsurfing or kitesurfing
    in the windy bays; Port Grimaud - Rent a paddleboard and explore the canals of
    this picturesque village; La Ciotat - Try snorkeling in the clear waters around
    the Île Verte.'
  - Change the playback speed
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
      name: persona relevance eval
      type: persona-relevance-eval
    metrics:
    - type: pearson_cosine
      value: 0.8870874250117823
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.8898791266492307
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
    'Plan a trip of 4 days for a group of 10 college friends.',
    'Culinary Experiences',
    'Change the playback speed',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.8710, 0.0099],
#         [0.8710, 1.0000, 0.0236],
#         [0.0099, 0.0236, 1.0000]])
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

* Dataset: `persona-relevance-eval`
* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.8871     |
| **spearman_cosine** | **0.8899** |

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

* Size: 209 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 209 samples:
  |         | sentence_0                                                                         | sentence_1                                                                         | label                                                          |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             | float                                                          |
  | details | <ul><li>min: 14 tokens</li><li>mean: 18.89 tokens</li><li>max: 33 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 54.62 tokens</li><li>max: 209 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.61</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                            | sentence_1                                         | label            |
  |:--------------------------------------------------------------------------------------|:---------------------------------------------------|:-----------------|
  | <code>Travel Planner: Plan a trip of 4 days for a group of 10 college friends.</code> | <code>Arles: A Roman Treasure</code>               | <code>0.1</code> |
  | <code>Travel Planner: Plan a trip of 4 days for a group of 10 college friends.</code> | <code>Nice: The Jewel of the French Riviera</code> | <code>0.1</code> |
  | <code>Travel Planner: Plan a trip of 4 days for a group of 10 college friends.</code> | <code>Nice: The Jewel of the French Riviera</code> | <code>0.1</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `num_train_epochs`: 30
- `fp16`: True
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
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
- `num_train_epochs`: 30
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
- `fp16`: True
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
| Epoch   | Step | persona-relevance-eval_spearman_cosine |
|:-------:|:----:|:--------------------------------------:|
| 0.4286  | 3    | 0.5355                                 |
| 0.8571  | 6    | 0.6371                                 |
| 1.0     | 7    | 0.6533                                 |
| 1.2857  | 9    | 0.6894                                 |
| 1.7143  | 12   | 0.7428                                 |
| 2.0     | 14   | 0.7760                                 |
| 2.1429  | 15   | 0.7842                                 |
| 2.5714  | 18   | 0.8009                                 |
| 3.0     | 21   | 0.8150                                 |
| 3.4286  | 24   | 0.8230                                 |
| 3.8571  | 27   | 0.8118                                 |
| 4.0     | 28   | 0.8128                                 |
| 4.2857  | 30   | 0.8122                                 |
| 4.7143  | 33   | 0.8185                                 |
| 5.0     | 35   | 0.8139                                 |
| 5.1429  | 36   | 0.8119                                 |
| 5.5714  | 39   | 0.8255                                 |
| 6.0     | 42   | 0.8391                                 |
| 6.4286  | 45   | 0.8374                                 |
| 6.8571  | 48   | 0.8287                                 |
| 7.0     | 49   | 0.8302                                 |
| 7.2857  | 51   | 0.8303                                 |
| 7.7143  | 54   | 0.8293                                 |
| 8.0     | 56   | 0.8234                                 |
| 8.1429  | 57   | 0.8256                                 |
| 8.5714  | 60   | 0.8248                                 |
| 9.0     | 63   | 0.8276                                 |
| 9.4286  | 66   | 0.8293                                 |
| 9.8571  | 69   | 0.8303                                 |
| 10.0    | 70   | 0.8303                                 |
| 10.2857 | 72   | 0.8356                                 |
| 10.7143 | 75   | 0.8379                                 |
| 11.0    | 77   | 0.8367                                 |
| 11.1429 | 78   | 0.8394                                 |
| 11.5714 | 81   | 0.8430                                 |
| 12.0    | 84   | 0.8440                                 |
| 12.4286 | 87   | 0.8483                                 |
| 12.8571 | 90   | 0.8529                                 |
| 13.0    | 91   | 0.8519                                 |
| 13.2857 | 93   | 0.8519                                 |
| 13.7143 | 96   | 0.8542                                 |
| 14.0    | 98   | 0.8573                                 |
| 14.1429 | 99   | 0.8595                                 |
| 14.5714 | 102  | 0.8645                                 |
| 15.0    | 105  | 0.8655                                 |
| 15.4286 | 108  | 0.8655                                 |
| 15.8571 | 111  | 0.8655                                 |
| 16.0    | 112  | 0.8642                                 |
| 16.2857 | 114  | 0.8642                                 |
| 16.7143 | 117  | 0.8632                                 |
| 17.0    | 119  | 0.8632                                 |
| 17.1429 | 120  | 0.8676                                 |
| 17.5714 | 123  | 0.8699                                 |
| 18.0    | 126  | 0.8793                                 |
| 18.4286 | 129  | 0.8783                                 |
| 18.8571 | 132  | 0.8793                                 |
| 19.0    | 133  | 0.8783                                 |
| 19.2857 | 135  | 0.8846                                 |
| 19.7143 | 138  | 0.8859                                 |
| 20.0    | 140  | 0.8849                                 |
| 20.1429 | 141  | 0.8859                                 |
| 20.5714 | 144  | 0.8863                                 |
| 21.0    | 147  | 0.8853                                 |
| 21.4286 | 150  | 0.8853                                 |
| 21.8571 | 153  | 0.8863                                 |
| 22.0    | 154  | 0.8853                                 |
| 22.2857 | 156  | 0.8863                                 |
| 22.7143 | 159  | 0.8853                                 |
| 23.0    | 161  | 0.8863                                 |
| 23.1429 | 162  | 0.8853                                 |
| 23.5714 | 165  | 0.8853                                 |
| 24.0    | 168  | 0.8853                                 |
| 24.4286 | 171  | 0.8899                                 |


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