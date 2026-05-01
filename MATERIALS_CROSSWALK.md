# Materials crosswalk

Source-to-destination mapping for every artifact migrated from the
Geneva 2026 live-course repository
(`/home/simon/projects/lectures/Deep_Learning_Econ_Finance_Geneva_2026`)
into this public repository.

Inclusion rule: an item is migrated if it is referenced in the source
`README.md`, directly or transitively (per `plan.md` §1.0).

The destination layout is **17 core lectures plus 3 toolkit modules**.
One Geneva source slide deck maps to one numbered destination item;
items previously carved into fragments have been consolidated.

Status legend:

- `migrated` — copied into the public tree at the destination shown.
- `excluded:not_referenced_in_source_readme` — present in the source
  tree but not referenced in the source README; not redistributed.
- `excluded:build_artifact` — LaTeX intermediates, caches, etc.
- `excluded:private` — author's private working notes / agent state.

Notebooks are migrated **without re-execution**; outputs are preserved
verbatim from the source repository. The lecture-header markdown cell
and the `RUN_MODE = "smoke"` switch are added in a follow-up pass.

## 1. Slides

| Source | Destination | Status |
|---|---|---|
| `lectures/day1/slides/01_Intro_to_DeepLearning.{pdf,tex}` | `lectures/lecture_02_B01_intro_deep_learning/slides/` | migrated |
| `lectures/day1/slides/figures/` | `lectures/lecture_02_B01_intro_deep_learning/slides/figures/` | migrated |
| `lectures/day2/slides/02_DeepEquilibriumNets.{pdf,tex}` | `lectures/lecture_03_B02_deep_equilibrium_nets/slides/` | migrated |
| `lectures/day2/slides/figures/` | `lectures/lecture_03_B02_deep_equilibrium_nets/slides/figures/` | migrated |
| `lectures/day3/slides/03_IRBC.{pdf,tex}` | `lectures/lecture_04_B03_irbc_with_deqns/slides/` | migrated |
| `lectures/day3/slides/04_Neural_Architecture_Search.{pdf,tex}` | `lectures/lecture_05_B04_nas_loss_normalization/slides/` | migrated |
| `lectures/day3/slides/05_Loss_Normalization.{pdf,tex}` | `lectures/lecture_05_B04_nas_loss_normalization/slides/` | migrated |
| `lectures/day3/slides/figures/` | `lectures/lecture_04_B03_irbc_with_deqns/slides/figures/` and `lectures/lecture_05_B04_nas_loss_normalization/slides/figures/` | migrated |
| `lectures/day4/slides/05b_AutoDiff_for_DEQN.{pdf,tex}` | `lectures/lecture_06_B05_autodiff_for_deqns/slides/` | migrated |
| `lectures/day4/slides/06_SequenceSpace_DEQNs.{pdf,tex}` | `lectures/lecture_07_B06_sequence_space_deqns/slides/` | migrated |
| `lectures/day4/slides/07_OLG_Models_DEQNs.{pdf,tex}` | `lectures/lecture_08_B07_olg_models_deqns/slides/` | migrated |
| `lectures/day4/slides/08_Heterogeneous_Agents_Youngs_Method.{pdf,tex}` | `lectures/lecture_09_B08_heterogeneous_agents_youngs_method/slides/` | migrated (newly in scope as L09 take-home item) |
| `lectures/day5/slides/05_Agentic_Programming.{pdf,tex}` | `toolkit/toolkit_01_T1_agentic_research_coding_loop/slides/` and `toolkit/toolkit_02_T2_project_memory_agents_hooks/slides/` | migrated (one source deck, two toolkit slots: T1 covers slot 1, T2 covers slot 2) |
| `lectures/day5/slides/05_Agentic_Programming_Exercises.{pdf,tex}` | `toolkit/toolkit_03_T3_agentic_programming_exercises/slides/` | migrated (newly in scope as T3) |
| `lectures/day6/slides/06_PINNs.{pdf,tex}` | `lectures/lecture_10_B09_pinns/slides/` | migrated |
| `lectures/day6/slides/07_CT_Heterogeneous_Agents_Theory.{pdf,tex}` | `lectures/lecture_11_B10_continuous_time_ha_theory/slides/` | migrated |
| `lectures/day6/slides/08_CT_Heterogeneous_Agents_Numerical.{pdf,tex}` | `lectures/lecture_12_B11_continuous_time_ha_numerics/slides/` | migrated |
| `lectures/day6/slides/fig/day6_ext/` | `lectures/lecture_10_B09_pinns/slides/fig/day6_ext/` | migrated |
| `lectures/day7/slides/07_Surrogates_and_GPs.{pdf,tex}` | `lectures/lecture_13_B12_surrogates_and_gps/slides/` | migrated |
| `lectures/day7/slides/08_Exercise_Structural_Estimation.{pdf,tex}` | `lectures/lecture_14_B13_structural_estimation_smm/slides/` | migrated |
| `lectures/day7/slides/gp_active_learning.pdf` | `lectures/lecture_13_B12_surrogates_and_gps/slides/gp_active_learning.pdf` | migrated (linked from L13 as supplementary) |
| `lectures/day7/slides/fig/` | `lectures/lecture_13_B12_surrogates_and_gps/slides/fig/` and `lectures/lecture_14_B13_structural_estimation_smm/slides/fig/` | migrated |
| `lectures/day8/slides/08_Climate_Economics_IAMs.{pdf,tex}` | `lectures/lecture_15_B14_climate_economics_iams/slides/` | migrated |
| `lectures/day8/slides/09_Deep_UQ_and_Optimal_Policies.{pdf,tex}` | `lectures/lecture_16_B15_deep_uq_pareto_improving_policy/slides/` | migrated |
| `lectures/day8/slides/10_Wrap_Up.{pdf,tex}` | `lectures/lecture_17_B16_course_wrap_up/slides/` | migrated |
| `lectures/day8/slides/fig/` | duplicated to L15 and L17 `slides/fig/` | migrated |

### Excluded slide decks

| Source | Status |
|---|---|
| `lectures/day2/slides/00_Recap_Day1.{pdf,tex}` | excluded:not_referenced_in_source_readme (live-class recap) |
| `lectures/day3/slides/00_Recap_Day2.{pdf,tex}` | excluded:not_referenced_in_source_readme |
| `lectures/day4/slides/00_Recap_Day3.{pdf,tex}` | excluded:not_referenced_in_source_readme |
| `lectures/day6/slides/00_Recap_Day5.{pdf,tex}` | excluded:not_referenced_in_source_readme |
| `lectures/day7/slides/00_Recap_Day6.{pdf,tex}` | excluded:not_referenced_in_source_readme |
| `lectures/day8/slides/00_Recap_Day7.{pdf,tex}` | excluded:not_referenced_in_source_readme |
| `lecture_notes/gp_active_learning.pdf` | excluded:not_referenced_in_source_readme (live `gp_active_learning.pdf` ships under L13 instead) |
| `lecture_notes/gp_vfi_2d_active_benchmark.pdf` | excluded:not_referenced_in_source_readme |
| `lecture_notes/joint_*.pdf` | excluded:not_referenced_in_source_readme |
| `lecture_notes/tracecheck.pdf` | excluded:build_artifact |

## 2. Notebooks

### Day 1 → Lecture 02 (Introduction to deep learning)

| Source | Destination | Status |
|---|---|---|
| `lectures/day1/code/01_BasicML_intro.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/core/lecture_02_B01_01_BasicML_intro.ipynb` | migrated (core) |
| `lectures/day1/code/02_GradientDescent_and_StochasticGradientDescent.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/core/lecture_02_B01_02_GradientDescent_and_StochasticGradientDescent.ipynb` | migrated (core) |
| `lectures/day1/code/SGD_data.txt` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/core/SGD_data.txt` | migrated (asset) |
| `lectures/day1/code/03_Double_Descent.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/core/lecture_02_B01_03_Double_Descent.ipynb` | migrated (core) |
| `lectures/day1/code/04_Gentle_DNN.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/core/lecture_02_B01_04_Gentle_DNN.ipynb` | migrated (core) |
| `lectures/day1/code/05_Tensorboard.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/extensions/lecture_02_B01_05_Tensorboard.ipynb` | migrated (extension) |
| `lectures/day1/code/06_PyTorch_intro.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/core/lecture_02_B01_06_PyTorch_intro.ipynb` | migrated (core) |
| `lectures/day1/code/07_Genz_Approximation_and_Loss_Functions.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/core/lecture_02_B01_07_Genz_Approximation_and_Loss_Functions.ipynb` | migrated (core) |
| `lectures/day1/code/08_MLP_LSTM_Transformer_Edgeworth_Cycles.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/core/lecture_02_B01_08_MLP_LSTM_Transformer_Edgeworth_Cycles.ipynb` | migrated (core) |
| `lectures/day1/code/09_Transformer_InContext_AR1.ipynb` | `lectures/lecture_02_B01_intro_deep_learning/notebooks/extensions/lecture_02_B01_09_Transformer_InContext_AR1.ipynb` | migrated (extension) |

### Day 2 → Lecture 03 (Deep Equilibrium Nets)

| Source | Destination | Status |
|---|---|---|
| `lectures/day2/code/01_Brock_Mirman_1972_DEQN.ipynb` | `lectures/lecture_03_B02_deep_equilibrium_nets/notebooks/core/lecture_03_B02_01_Brock_Mirman_1972_DEQN.ipynb` | migrated (core) |
| `lectures/day2/code/02_Brock_Mirman_Uncertainty_DEQN.ipynb` | `lectures/lecture_03_B02_deep_equilibrium_nets/notebooks/core/lecture_03_B02_02_Brock_Mirman_Uncertainty_DEQN.ipynb` | migrated (core) |
| `lectures/day2/code/03_DEQN_Exercises_Blanks.ipynb` | `lectures/lecture_03_B02_deep_equilibrium_nets/notebooks/exercises/lecture_03_B02_03_DEQN_Exercises_Blanks.ipynb` | migrated (exercise) |
| `lectures/day2/code/04_DEQN_Exercises_Solutions.ipynb` | `lectures/lecture_03_B02_deep_equilibrium_nets/notebooks/solutions/lecture_03_B02_04_DEQN_Exercises_Solutions.ipynb` | migrated (solution) |
| `lectures/day2/code/05_StochasticBM_LossComparison.ipynb` | `lectures/lecture_03_B02_deep_equilibrium_nets/notebooks/core/lecture_03_B02_05_StochasticBM_LossComparison.ipynb` | migrated (core) |

### Day 3 → Lectures 04 (IRBC) and 05 (NAS / Loss Normalization)

| Source | Destination | Status |
|---|---|---|
| `lectures/day3/code/01_IRBC_DEQN.ipynb` | `lectures/lecture_04_B03_irbc_with_deqns/notebooks/core/lecture_04_B03_01_IRBC_DEQN.ipynb` | migrated (core) |
| `lectures/day3/code/02_NAS_Random_Search_10D.ipynb` | `lectures/lecture_05_B04_nas_loss_normalization/notebooks/core/lecture_05_B04_02_NAS_Random_Search_10D.ipynb` | migrated (core) |
| `lectures/day3/code/03_NAS_RandomSearch_Hyperband.ipynb` | `lectures/lecture_05_B04_nas_loss_normalization/notebooks/core/lecture_05_B04_03_NAS_RandomSearch_Hyperband.ipynb` | migrated (core) |
| `lectures/day3/code/04_Loss_Normalization.ipynb` | `lectures/lecture_05_B04_nas_loss_normalization/notebooks/core/lecture_05_B04_04_Loss_Normalization.ipynb` | migrated (core) |
| `lectures/day3/code/05_IRBC_Exercise.ipynb` | `lectures/lecture_05_B04_nas_loss_normalization/notebooks/exercises/lecture_05_B04_05_IRBC_Exercise.ipynb` | migrated (exercise) |

### Day 4 → Lectures 06 (AutoDiff), 07 (Sequence-Space), 08 (OLG), 09 (Young's method)

| Source | Destination | Status |
|---|---|---|
| `lectures/day4/code/01_AutoDiff_Analytical_Examples.ipynb` | `lectures/lecture_06_B05_autodiff_for_deqns/notebooks/core/lecture_06_B05_01_AutoDiff_Analytical_Examples.ipynb` | migrated (core) |
| `lectures/day4/code/02_Brock_Mirman_AutoDiff_DEQN.ipynb` | `lectures/lecture_06_B05_autodiff_for_deqns/notebooks/core/lecture_06_B05_02_Brock_Mirman_AutoDiff_DEQN.ipynb` | migrated (core) |
| `lectures/day4/code/03_Brock_Mirman_Uncertainty_AutoDiff_DEQN.ipynb` | `lectures/lecture_06_B05_autodiff_for_deqns/notebooks/core/lecture_06_B05_03_Brock_Mirman_Uncertainty_AutoDiff_DEQN.ipynb` | migrated (core) |
| `lectures/day4/code/04_IRBC_AutoDiff_DEQN.ipynb` | `lectures/lecture_06_B05_autodiff_for_deqns/notebooks/extensions/lecture_06_B05_04_IRBC_AutoDiff_DEQN.ipynb` | migrated (extension) |
| `lectures/day4/code/05_SequenceSpace_BrockMirman.ipynb` | `lectures/lecture_07_B06_sequence_space_deqns/notebooks/core/lecture_07_B06_05_SequenceSpace_BrockMirman.ipynb` | migrated (core) |
| `lectures/day4/code/05b_SequenceSpace_IRBC.ipynb` | `lectures/lecture_07_B06_sequence_space_deqns/notebooks/extensions/lecture_07_B06_05b_SequenceSpace_IRBC.ipynb` | migrated (extension) |
| `lectures/day4/code/06_SequenceSpace_KrusellSmith.ipynb` | `lectures/lecture_07_B06_sequence_space_deqns/notebooks/core/lecture_07_B06_06_SequenceSpace_KrusellSmith.ipynb` | migrated (core) |
| `lectures/day4/code/07_OLG_Analytic_DEQN.ipynb` | `lectures/lecture_08_B07_olg_models_deqns/notebooks/core/lecture_08_B07_07_OLG_Analytic_DEQN.ipynb` | migrated (core) |
| `lectures/day4/code/08_OLG_Benchmark_DEQN.ipynb` | `lectures/lecture_08_B07_olg_models_deqns/notebooks/core/lecture_08_B07_08_OLG_Benchmark_DEQN.ipynb` | migrated (core) |
| `lectures/day4/code/09_OLG_Exercise.ipynb` | `lectures/lecture_08_B07_olg_models_deqns/notebooks/exercises/lecture_08_B07_09_OLG_Exercise.ipynb` | migrated (exercise) |
| `lectures/day4/code/10_Youngs_Method_Examples.ipynb` | `lectures/lecture_09_B08_heterogeneous_agents_youngs_method/notebooks/core/lecture_09_B08_10_Youngs_Method_Examples.ipynb` | migrated (core) |
| `lectures/day4/code/11_Continuum_of_Agents_DEQN.ipynb` | `lectures/lecture_09_B08_heterogeneous_agents_youngs_method/notebooks/core/lecture_09_B08_11_Continuum_of_Agents_DEQN.ipynb` | migrated (core) |
| `lectures/day4/code/12_KrusellSmith_DeepLearning.ipynb` | `lectures/lecture_09_B08_heterogeneous_agents_youngs_method/notebooks/extensions/lecture_09_B08_12_KrusellSmith_DeepLearning.ipynb` | migrated (extension) |
| `lectures/day4/code/KrusellSmith_Tutorial_CPU.ipynb` | `lectures/lecture_07_B06_sequence_space_deqns/notebooks/extensions/lecture_07_B06_KrusellSmith_Tutorial_CPU.ipynb` | migrated (extension; **borrowed/adapted**, upstream JAX tutorial; preserve upstream notice) |

### Day 5 → Toolkits T1, T2, T3

| Source | Destination | Status |
|---|---|---|
| `lectures/day5/agentic_ai_lecture_syllabus.md` | `toolkit/toolkit_01_T1_agentic_research_coding_loop/notes/agentic_ai_lecture_syllabus.md` | migrated |
| `lectures/day5/code/README.md` | `toolkit/README.md` | migrated |
| `lectures/day5/code/exercise_prompts.md` | `toolkit/toolkit_01_T1_agentic_research_coding_loop/exercises/exercise_prompts.md` | migrated |
| `lectures/day5/code/exercise_solutions.md` | `toolkit/toolkit_01_T1_agentic_research_coding_loop/solutions/exercise_solutions.md` | migrated |
| `lectures/day5/code/generate_synthetic_data.py` | `toolkit/toolkit_01_T1_agentic_research_coding_loop/code/generate_synthetic_data.py` | migrated |
| `lectures/day5/code/mincer_demo.py` | `toolkit/toolkit_01_T1_agentic_research_coding_loop/code/mincer_demo.py` | migrated |
| `lectures/day5/code/data/synthetic_panel.csv` | `toolkit/toolkit_01_T1_agentic_research_coding_loop/code/data/synthetic_panel.csv` | migrated |
| `lectures/day5/code/outputs/mincer_{figure.pdf,table.tex}` | `toolkit/toolkit_01_T1_agentic_research_coding_loop/code/outputs/` | migrated |
| `lectures/day5/code/CLAUDE_md_template.md` | `toolkit/toolkit_02_T2_project_memory_agents_hooks/templates/CLAUDE_md_template.md` | migrated |
| `lectures/day5/code/example_skill/SKILL.md` | `toolkit/toolkit_02_T2_project_memory_agents_hooks/example_skill/SKILL.md` | migrated |
| `lectures/day5/code/example_skill_strategic_revision/SKILL.md` | `toolkit/toolkit_02_T2_project_memory_agents_hooks/example_skill_strategic_revision/SKILL.md` | migrated |
| `lectures/day5/code/example_subagent/*.md` | `toolkit/toolkit_02_T2_project_memory_agents_hooks/example_subagent/` | migrated |
| `lectures/day5/code/example_hooks/settings.json` | `toolkit/toolkit_02_T2_project_memory_agents_hooks/example_hooks/settings.json` | migrated |

### Day 6 → Lectures 10 (PINNs) and 12 (CT-HA numerics)

| Source | Destination | Status |
|---|---|---|
| `lectures/day6/code/01_ODE_PINN_ZeroBCs.ipynb` | `lectures/lecture_10_B09_pinns/notebooks/core/lecture_10_B09_01_ODE_PINN_ZeroBCs.ipynb` | migrated (core) |
| `lectures/day6/code/02_ODE_PINN_SoftVsHardBCs.ipynb` | `lectures/lecture_10_B09_pinns/notebooks/core/lecture_10_B09_02_ODE_PINN_SoftVsHardBCs.ipynb` | migrated (core) |
| `lectures/day6/code/03_PDE_PINN_Poisson2D.ipynb` | `lectures/lecture_10_B09_pinns/notebooks/core/lecture_10_B09_03_PDE_PINN_Poisson2D.ipynb` | migrated (core) |
| `lectures/day6/code/04_Cake_Eating_HJB_PINN.ipynb` | `lectures/lecture_10_B09_pinns/notebooks/core/lecture_10_B09_04_Cake_Eating_HJB_PINN.ipynb` | migrated (core) |
| `lectures/day6/code/05_Black_Scholes_PINN.ipynb` | `lectures/lecture_10_B09_pinns/notebooks/core/lecture_10_B09_05_Black_Scholes_PINN.ipynb` | migrated (core) |
| `lectures/day6/code/06_PE_Discrete_HJB_PINN.ipynb` | `lectures/lecture_12_B11_continuous_time_ha_numerics/notebooks/core/lecture_12_B11_06_PE_Discrete_HJB_PINN.ipynb` | migrated (core) |
| `lectures/day6/code/07_PE_Diffusion_HJB_PINN.ipynb` | `lectures/lecture_12_B11_continuous_time_ha_numerics/notebooks/core/lecture_12_B11_07_PE_Diffusion_HJB_PINN.ipynb` | migrated (core) |
| `lectures/day6/code/08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb` | `lectures/lecture_12_B11_continuous_time_ha_numerics/notebooks/core/lecture_12_B11_08_Aiyagari_Continuous_Time_FD_and_PINN_PyTorch.ipynb` | migrated (core) |
| `lectures/day6/code/09_PINN_Exercise.ipynb` | `lectures/lecture_12_B11_continuous_time_ha_numerics/notebooks/exercises/lecture_12_B11_09_PINN_Exercise.ipynb` | migrated (exercise) |

### Day 7 → Lectures 13 (Surrogates and GPs) and 14 (SMM)

| Source | Destination | Status |
|---|---|---|
| `lectures/day7/code/01_Surrogate_Primer.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/core/lecture_13_B12_01_Surrogate_Primer.ipynb` | migrated (core) |
| `lectures/day7/code/02_GP_and_BAL.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/core/lecture_13_B12_02_GP_and_BAL.ipynb` | migrated (core) |
| `lectures/day7/code/03_Structural_Estimation_BM.ipynb` | `lectures/lecture_14_B13_structural_estimation_smm/notebooks/core/lecture_14_B13_03_Structural_Estimation_BM.ipynb` | migrated (core) |
| `lectures/day7/code/03b_Structural_Estimation_BM_Joint.ipynb` | `lectures/lecture_14_B13_structural_estimation_smm/notebooks/extensions/lecture_14_B13_03b_Structural_Estimation_BM_Joint.ipynb` | migrated (extension) |
| `lectures/day7/code/04_GP_Value_Function_Iteration.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/core/lecture_13_B12_04_GP_Value_Function_Iteration.ipynb` | migrated (core) |
| `lectures/day7/code/05_Active_Subspace_2D.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/core/lecture_13_B12_05_Active_Subspace_2D.ipynb` | migrated (core) |
| `lectures/day7/code/06_Active_Subspace_10D.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/core/lecture_13_B12_06_Active_Subspace_10D.ipynb` | migrated (core) |
| `lectures/day7/code/07_Active_Subspace_Nonlinear.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/extensions/lecture_13_B12_07_Active_Subspace_Nonlinear.ipynb` | migrated (extension) |
| `lectures/day7/code/08_Deep_Kernel_Learning.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/core/lecture_13_B12_08_Deep_Kernel_Learning.ipynb` | migrated (core) |
| `lectures/day7/code/09_Deep_Active_Subspace_Ridge.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/extensions/lecture_13_B12_09_Deep_Active_Subspace_Ridge.ipynb` | migrated (extension) |
| `lectures/day7/code/10_Deep_AS_vs_Linear_AS_Borehole.ipynb` | `lectures/lecture_13_B12_surrogates_and_gps/notebooks/extensions/lecture_13_B12_10_Deep_AS_vs_Linear_AS_Borehole.ipynb` | migrated (extension) |
| `lectures/day7/code/plot_cell_*.png` | — | excluded:not_referenced_in_source_readme |

### Day 8 → Lecture 15 (Climate / IAMs)

| Source | Destination | Status |
|---|---|---|
| `lectures/day8/code/01_Climate_Exercise.ipynb` | `lectures/lecture_15_B14_climate_economics_iams/notebooks/exercises/lecture_15_B14_01_Climate_Exercise.ipynb` | migrated (exercise) |
| `lectures/day8/code/02_DICE_DEQN_Library_Port.ipynb` | `lectures/lecture_15_B14_climate_economics_iams/notebooks/core/lecture_15_B14_02_DICE_DEQN_Library_Port.ipynb` | migrated (core) |
| `lectures/day8/code/03_Stochastic_DICE_DEQN.ipynb` | `lectures/lecture_15_B14_climate_economics_iams/notebooks/extensions/lecture_15_B14_03_Stochastic_DICE_DEQN.ipynb` | migrated (extension) |

### Excluded notebooks and code (Day 8 research artefacts)

| Source | Status |
|---|---|
| `lectures/day8/code/03_Stochastic_DICE_DEQN_codex.ipynb` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/04_DICE_DEQN_EpsteinZin{,_Weather}{.ipynb,_codex.ipynb}` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/05_DICE_DEQN_EpsteinZin{,_codex}.ipynb` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/06_DICE_DEQN_Surrogate.ipynb` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/07_Surrogate_Verification.ipynb` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/08_DICE_Surrogate_TwoParam.ipynb` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/dice_deqn_codex_lib.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/dice_2p_surrogate_lib.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/compute_dice_2p_gp_sobol.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/refine_codex_surrogate_slices.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/run_codex_surrogate_experiment.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/train_codex_surrogate_*.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/train_dice_2p_pointsolutions.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/train_dice_2p_surrogate.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/validate_dice_2p_surrogate.py` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/problem.md` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/plot_cell_*.png` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/archive/` | excluded:not_referenced_in_source_readme |
| `lectures/day8/code/_pt_solutions/` | excluded:not_referenced_in_source_readme |

## 3. Lecture script and bibliography

| Source | Destination | Status |
|---|---|---|
| `lecture_notes/lecture_script.tex` | `lecture_script/lecture_script.tex` | migrated |
| `lecture_notes/lecture_script.pdf` | `lecture_script/lecture_script.pdf` | migrated |
| `lecture_notes/loss_kernel_convergence.png` | `lecture_script/loss_kernel_convergence.png` | migrated |
| `bib/bib_econ.bib` | `readings/bibliography.bib` | migrated |
| `lecture_notes/CITATION_AUDIT_*.md` | — | excluded:private (author working notes) |

## 4. Hero / overview / pre-course assets

| Source | Destination | Status |
|---|---|---|
| `fig/deep_learning_dynamic_models_hero.png` | `assets/hero/deep_learning_dynamic_models_hero.png` | migrated |
| `fig/cover_*.{png,svg}` | — | excluded:not_referenced_in_source_readme (alternative covers) |
| `python_refresher/*.ipynb`, `README.md`, `temp_price.csv` | `lectures/lecture_01_B00_orientation_setup_reproducibility/python_refresher/` | migrated |

## 5. Tools / scripts

| Source | Destination | Status |
|---|---|---|
| `tools/normalize_headers.py` | `scripts/migration/normalize_headers.py` | migrated (seed for `validate_headers.py`) |
| `tools/notebook_attribution.csv` | `scripts/migration/notebook_attribution.csv` | migrated (reference) |
| `tools/notebook_chapter_map.csv` | `scripts/migration/notebook_chapter_map.csv` | migrated (reference) |

## 6. Readings (link-only by default)

Reading PDFs from `lectures/dayN/readings/` are **not** copied to the
public tree by default. Each is recorded as a link in
`readings/links_by_lecture/lecture_XX_BYY.md` and a BibTeX entry in
`readings/bibliography.bib`. PDFs move into `readings/allowed_pdfs/`
on a per-paper basis after license clearance.

| Source | Destination | Status |
|---|---|---|
| `lectures/day1/readings/{taming,Murphy_2022_Probabilistic_Machine_Learning_Introduction,James_etal_2021_Introduction_to_Statistical_Learning_R_v2}.pdf` | `readings/links_by_lecture/lecture_02_B01.md` | pending license review (link_only by default) |
| `lectures/day2/readings/Azinovic_Gaegauf_Scheidegger_2022_DEQN.pdf` | `readings/links_by_lecture/lecture_03_B02.md` | pending license review |
| `lectures/day3/readings/Elsken_Metzen_Hutter_2019_NAS_Survey.pdf` | `readings/links_by_lecture/lecture_05_B04.md` | pending license review |
| `lectures/day4/readings/{Young_2010,Method,MaliarMaliarWinant_2021_JME_preprint,DeepHAM_Han_Yang_E_2023,SequenceSpace_AZ}.pdf` | `readings/links_by_lecture/lecture_07_B06.md`, `lecture_09_B08.md` | pending license review |
| `lectures/day6/readings/Payne/*.pdf` | — | excluded:not_referenced_in_source_readme |
| `lectures/day7/readings/{DeepSurrogates_JFE,JPE_Macro,ML_DP}.pdf` | `readings/links_by_lecture/lecture_13_B12.md`, `lecture_16_B15.md` | pending license review |
| `lectures/day8/readings/{CDICE_Restud_production,CDICE_Restud_production_appendix,DeepUQ_with_an_application_to_IAM,JPE_Macro,CaiLontzek}.pdf` | `readings/links_by_lecture/lecture_15_B14.md`, `lecture_16_B15.md` | pending license review |

## 7. Source-repository root-level files

| Source | Destination | Status |
|---|---|---|
| `README.md` | day-by-day timetable extracted to `legacy/Geneva2026_TIMETABLE.md`; public portal rewritten as `README.md` | migrated (timetable); rewritten (portal) |
| `LICENCE` | replaced by `LICENSE` (MIT, code) and `LICENSE-content.md` (CC0, content) | rewritten |
| `requirements.txt` | rewritten with explanatory header and `pyyaml` added | migrated and audited |
| `README.pdf` | — | excluded:not_referenced_in_source_readme (rendered duplicate of source README) |
| `suggestion.md`, `TODO_review.md` | — | excluded:private |
| `codex_results/` | — | excluded:not_referenced_in_source_readme |
| `lecture_notes/.claude/`, `lectures/dayN/.claude/`, `lectures/dayN/code/.claude/` | — | excluded:private (agent state) |
| `lecture_notes/{lecture_script.aux, .bbl, .blg, .log, .out, .toc, tracecheck.{aux,log,out,pdf,toc}, texput.log}` | — | excluded:build_artifact |

## 8. Items pending follow-up work

- **Notebook lecture headers and `RUN_MODE` cells**: per `plan.md` §1.6
  / §11.1, every first-party notebook needs an updated markdown header
  cell (with the new lecture ID) and a `RUN_MODE = "smoke"` switch.
  Headers and switches are added in a follow-up pass; notebooks are
  not re-executed.
- **Slide PDFs**: `.tex` files have changed since the last compile
  (live-class strip, title updates). PDFs in this commit are stale
  relative to their `.tex` and will be recompiled in a separate
  user-authorized pass.
- **`src/dlef/` extraction**: empty subpackages exist; populated only
  if duplication across notebooks becomes obvious.
