from __future__ import annotations

import hashlib
import json
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tests" / "fixtures" / "methodological_navigation"
OUT.mkdir(parents=True, exist_ok=True)
NS = uuid.UUID("ec4dfa2d-0c37-4e6b-8d45-e07124947f72")
SOURCE_ID = "spec022-design-synthesis"


def uid(label: str) -> str:
    return str(uuid.uuid5(NS, label))


def pred(name: str) -> dict:
    return {"predicate": name, "arguments": {}}


def all_of(*names: str) -> dict:
    return {"all": [pred(name) for name in names]}


def any_of(*names: str) -> dict:
    return {"any": [pred(name) for name in names]}


def asset(key, title, kind, purpose, terms, cues, functions, applicability=None):
    return {
        "applicability": applicability,
        "asset_id": uid(f"asset:{key}"),
        "components": [],
        "context_requirements": [],
        "governance_status": "CANDIDATE",
        "intrinsic_kind": kind,
        "limitations": [],
        "narrative_facets": [],
        "provenance_source_ids": [SOURCE_ID],
        "purpose": purpose,
        "reasoning_functions": functions,
        "retrieval_profile": {
            "aliases": [],
            "lexical_terms": terms,
            "negative_cues": [],
            "semantic_cues": cues,
        },
        "revision_id": uid(f"asset-revision:{key}:1"),
        "revision_no": 1,
        "rules": [],
        "scope": None,
        "semantic_checks": [],
        "stable_key": key,
        "title": title,
    }


ASSETS = [
    asset("target-definition", "Target Definition", "FRAMEWORK", "Define exactly what outcome is predicted or estimated and at what semantic horizon.", ["target definition", "outcome definition", "label definition"], ["clarify the exact outcome and label semantics before modelling"], ["QUESTION_TEMPLATE", "VALIDITY_CONSTRAINT"]),
    asset("unit-of-observation", "Unit of Observation", "FRAMEWORK", "Establish what one row or observation represents and how observations relate to entities and time.", ["unit of observation", "one row", "row represents"], ["identify the observational unit and entity structure of the dataset"], ["QUESTION_TEMPLATE", "DATA_STRUCTURE"]),
    asset("prediction-moment", "Prediction Moment", "CONCEPT", "Define the exact operational time at which a prediction must be produced.", ["prediction moment", "scoring cutoff", "prediction cutoff", "scoring time"], ["define when the prediction is made relative to available information"], ["VALIDITY_CONSTRAINT"], pred("project.use.requires_pre_outcome_prediction")),
    asset("prediction-time-feature-eligibility", "Prediction-Time Feature Eligibility", "RULE", "Require every predictor to be available by the operational prediction moment.", ["feature availability", "available at scoring", "known before prediction", "feature timing"], ["audit whether every candidate predictor exists before the scoring event"], ["VALIDITY_CONSTRAINT", "QUESTION_TEMPLATE"], all_of("project.use.requires_pre_outcome_prediction", "prediction.moment.is_defined")),
    asset("data-leakage", "Data Leakage", "FRAMEWORK", "Detect information entering training or evaluation that would not be legitimately available under the intended generalization regime.", ["data leakage", "label leakage", "train test leakage", "information leakage"], ["prevent unavailable or held-out information from contaminating modelling or evaluation"], ["VALIDITY_CONSTRAINT", "FAILURE_MODE"]),
    asset("temporal-leakage", "Temporal Leakage", "RULE", "Prevent future information from influencing earlier predictions, preprocessing, feature construction, or evaluation.", ["temporal leakage", "future information", "look ahead", "future data"], ["ensure future observations cannot influence earlier prediction or validation decisions"], ["VALIDITY_CONSTRAINT", "FAILURE_MODE"], all_of("project.generalization.is_future_facing", "prediction.moment.is_defined")),
    asset("train-validation-test-separation", "Train Validation Test Separation", "FRAMEWORK", "Keep model fitting, model selection, and final evaluation on properly separated data roles.", ["train validation test", "data split", "holdout", "validation split"], ["separate fitting selection and final evaluation data"], ["VALIDITY_CONSTRAINT", "DECISION_FRAMEWORK"]),
    asset("temporal-validation", "Temporal Validation", "FRAMEWORK", "Align validation ordering and cutoffs with a future-facing deployment claim.", ["temporal validation", "chronological validation", "time split", "rolling validation"], ["evaluate future deployment using past-to-future validation rather than random temporal mixing"], ["VALIDITY_CONSTRAINT", "EVALUATION_DESIGN"], all_of("project.generalization.is_future_facing", "prediction.moment.is_defined")),
    asset("repeated-entity-generalization", "Repeated-Entity Generalization", "FRAMEWORK", "Clarify whether repeated observations from the same entity may appear across fitting and evaluation and whether that matches the intended generalization target.", ["repeated entities", "same customer", "same patient", "entity generalization"], ["reason about repeated entities and whether evaluation should generalize to new periods or new entities"], ["VALIDITY_CONSTRAINT", "DATA_STRUCTURE"], pred("data.entities.repeat_across_rows")),
    asset("group-aware-validation", "Group-Aware Validation", "METHOD", "Keep related observations together when evaluation requires independence across entity groups.", ["group validation", "group split", "group k fold", "entity split"], ["split evaluation by entity or group when repeated records would otherwise cross folds"], ["EVALUATION_DESIGN"], pred("data.entities.repeat_across_rows")),
    asset("preprocessing-fit-isolation", "Preprocessing Fit Isolation", "RULE", "Fit learned preprocessing only on the fitting portion of each evaluation split.", ["preprocessing leakage", "fit imputer on train", "fit scaler on train", "pipeline leakage"], ["prevent imputation scaling encoding or other learned preprocessing from seeing validation or test data"], ["VALIDITY_CONSTRAINT", "FAILURE_MODE"]),
    asset("feature-selection-isolation", "Feature Selection Isolation", "RULE", "Perform supervised or data-adaptive feature selection inside the training and validation procedure rather than before it.", ["feature selection leakage", "select features on train", "feature selection inside cross validation"], ["keep feature selection from using validation test or full-label information"], ["VALIDITY_CONSTRAINT", "FAILURE_MODE"]),
    asset("missing-data", "Missing Data", "FRAMEWORK", "Characterize missingness patterns, mechanisms, affected variables, and modelling implications.", ["missing data", "missing values", "null values", "missingness"], ["inspect where data are missing and whether missingness carries process or measurement information"], ["DECISION_FRAMEWORK", "EVIDENCE_OPTION"]),
    asset("production-missingness-alignment", "Production Missingness Alignment", "RULE", "Compare development missingness patterns with the missingness expected or observed at deployment.", ["production missingness", "deployment missingness", "missingness shift", "missing data in production"], ["check whether missing-value patterns at deployment match the development data"], ["VALIDITY_CONSTRAINT", "MONITORING"], pred("data.production_missingness_profile.is_known")),
    asset("class-imbalance", "Class Imbalance", "FRAMEWORK", "Account for materially unequal class prevalence when interpreting evaluation and model behaviour.", ["class imbalance", "rare positive", "minority class", "class prevalence"], ["reason about unequal class prevalence and its consequences for modelling and evaluation"], ["DECISION_FRAMEWORK", "INTERPRETATION_GUIDANCE"], pred("target.class_prevalence.is_materially_imbalanced")),
    asset("minority-sensitive-metrics", "Minority-Sensitive Classification Metrics", "FRAMEWORK", "Use metrics that expose minority-class errors when accuracy or aggregate error can hide them.", ["precision recall", "recall", "f1", "pr auc", "minority metrics"], ["evaluate rare positive outcomes with metrics that expose minority performance"], ["EVALUATION_DESIGN", "INTERPRETATION_GUIDANCE"], pred("target.class_prevalence.is_materially_imbalanced")),
    asset("linear-logistic-baseline", "Linear Logistic Baseline", "METHOD", "Establish a transparent regularized or unregularized logistic-regression baseline for binary tabular prediction.", ["logistic regression baseline", "linear baseline", "simple classifier"], ["compare more flexible models against a transparent linear classification baseline"], ["MODEL_OPTION"], pred("project.task.is_supervised_classification")),
    asset("nonlinear-model-comparison", "Nonlinear Model-Family Comparison", "FRAMEWORK", "Compare justified nonlinear model families against the baseline when evidence suggests nonlinear structure may matter.", ["nonlinear model", "tree model", "model comparison", "nonlinear classifier"], ["compare flexible nonlinear model families when a linear baseline may miss structure"], ["MODEL_OPTION", "DECISION_FRAMEWORK"], pred("project.task.is_supervised_classification")),
    asset("probability-calibration", "Probability Calibration", "FRAMEWORK", "Assess whether predicted probabilities correspond to observed event frequencies when probabilities are used as probabilities.", ["probability calibration", "calibration curve", "reliability diagram", "calibrated probabilities"], ["verify that predicted risks are numerically meaningful probabilities for decisions"], ["EVALUATION_DESIGN", "INTERPRETATION_GUIDANCE"], pred("output.probability_used_as_probability")),
    asset("proper-scoring-rules", "Proper Probability Scoring Rules", "FRAMEWORK", "Evaluate probabilistic predictions with proper scoring rules such as log loss or Brier score when probability quality matters.", ["log loss", "brier score", "proper scoring rule", "probability score"], ["evaluate the quality of full probability predictions rather than only ranking or hard labels"], ["EVALUATION_DESIGN"], pred("output.probability_used_as_probability")),
    asset("threshold-selection", "Decision Threshold Selection", "FRAMEWORK", "Select a classification threshold from validation evidence and the operational decision objective rather than defaulting mechanically to 0.5.", ["decision threshold", "classification threshold", "operating point", "cutoff"], ["choose the action threshold using validation data and operational consequences"], ["DECISION_FRAMEWORK"], pred("decision.threshold_required")),
    asset("asymmetric-error-costs", "Asymmetric Error Costs", "FRAMEWORK", "Represent unequal costs or utilities of false positives and false negatives when selecting a decision rule.", ["false negative cost", "false positive cost", "asymmetric cost", "decision cost"], ["account for unequal error consequences in model and threshold decisions"], ["DECISION_FRAMEWORK", "INTERPRETATION_GUIDANCE"], pred("decision.costs_are_asymmetric")),
    asset("final-test-protection", "Final Test Protection", "RULE", "Keep the final test set untouched until all modelling and decision-selection choices are frozen.", ["final test", "locked test set", "untouched test", "test set protection"], ["preserve a final unbiased evaluation by preventing iterative selection on the test set"], ["VALIDITY_CONSTRAINT"]),
    asset("selection-evaluation-separation", "Selection and Evaluation Separation", "RULE", "Use validation evidence for model and policy selection and reserve final evaluation for the already-selected procedure.", ["model selection validation", "selection evaluation", "choose on validation", "evaluate once"], ["separate adaptive choice from final performance estimation"], ["VALIDITY_CONSTRAINT", "DECISION_FRAMEWORK"]),
    asset("distribution-shift", "Distribution Shift", "FRAMEWORK", "Assess whether deployment or new-regime data differ materially from development data in ways that can affect validity.", ["distribution shift", "data drift", "covariate shift", "deployment shift"], ["compare development and new-regime distributions when the data-generating process may have changed"], ["VALIDITY_CONSTRAINT", "MONITORING"], pred("data.distribution_shift.suspected_or_observed")),
    asset("measurement-regime-change", "Measurement Regime Change", "FRAMEWORK", "Reassess feature meaning, scale, missingness, and comparability after a collection or measurement-system change.", ["measurement change", "collection system change", "sensor units changed", "data collection change"], ["verify measurement comparability after a new instrument pipeline or collection regime is introduced"], ["VALIDITY_CONSTRAINT", "DATA_QUALITY"], pred("data.measurement_regime.changed")),
    asset("subgroup-robustness", "Subgroup Robustness", "FRAMEWORK", "Check performance and data quality across materially relevant subgroups when deployment requires reliable behaviour across them.", ["subgroup performance", "site performance", "group robustness", "slice analysis"], ["inspect whether model validity and data quality differ across deployment subgroups"], ["EVALUATION_DESIGN", "ROBUSTNESS"], pred("deployment.subgroup_reliability_required")),
    asset("revalidation-after-data-change", "Revalidation After Data Change", "RULE", "Re-run appropriate validation when a material collection, measurement, or distribution change can invalidate earlier evidence.", ["revalidation", "validate after data change", "retest model", "model revalidation"], ["repeat validation after material data or measurement changes rather than relying on stale evidence"], ["VALIDITY_CONSTRAINT", "MONITORING"], any_of("data.distribution_shift.suspected_or_observed", "data.measurement_regime.changed")),
]

RELATIONS = []
for i, (source, target, relation_type, rationale) in enumerate([
    ("prediction-time-feature-eligibility", "prediction-moment", "REQUIRES_CONCEPT", "Feature eligibility is defined relative to the prediction moment."),
    ("temporal-leakage", "prediction-moment", "REQUIRES_CONCEPT", "Temporal leakage is judged relative to the prediction cutoff."),
    ("temporal-validation", "prediction-moment", "REQUIRES_CONCEPT", "Temporal validation requires a defined prediction cutoff."),
    ("group-aware-validation", "repeated-entity-generalization", "USES_CONCEPT", "Group-aware splitting operationalizes an entity-generalization requirement."),
    ("feature-selection-isolation", "preprocessing-fit-isolation", "USES_CONCEPT", "Feature selection is one learned preprocessing step that must respect split isolation."),
    ("production-missingness-alignment", "missing-data", "USES_CONCEPT", "Production missingness alignment builds on missingness characterization."),
    ("minority-sensitive-metrics", "class-imbalance", "USES_CONCEPT", "Minority-sensitive metrics are activated by materially unequal prevalence."),
    ("nonlinear-model-comparison", "linear-logistic-baseline", "ALTERNATIVE_TO", "Nonlinear model families should be compared against a transparent linear baseline."),
    ("probability-calibration", "proper-scoring-rules", "USES_CONCEPT", "Calibration should be evaluated alongside proper probability scoring."),
    ("threshold-selection", "asymmetric-error-costs", "REQUIRES_CONCEPT", "Decision thresholds should reflect the operational error-cost structure when it is asymmetric."),
    ("final-test-protection", "selection-evaluation-separation", "USES_CONCEPT", "Final-test protection enforces separation between adaptive selection and final evaluation."),
    ("measurement-regime-change", "distribution-shift", "USES_CONCEPT", "Measurement changes can create distribution shifts that require explicit assessment."),
    ("revalidation-after-data-change", "distribution-shift", "REQUIRES_CONCEPT", "Observed distribution change can invalidate prior validation evidence."),
    ("revalidation-after-data-change", "measurement-regime-change", "REQUIRES_CONCEPT", "A material measurement-regime change can require revalidation."),
    ("subgroup-robustness", "distribution-shift", "USES_CONCEPT", "Aggregate shift can mask subgroup-specific degradation."),
], start=1):
    RELATIONS.append({
        "governance_status": "CANDIDATE",
        "provenance_source_ids": [SOURCE_ID],
        "rationale": rationale,
        "relation_id": uid(f"relation:{i}:{source}:{target}"),
        "relation_revision_id": uid(f"relation-revision:{i}:{source}:{target}:1"),
        "relation_type": relation_type,
        "revision_no": 1,
        "scope": None,
        "source_ref": {"asset_key": source},
        "target_ref": {"asset_key": target},
    })

UNIVERSE = {
    "assets": ASSETS,
    "bundle_kind": "BENCHMARK_FIXTURE",
    "collections": [{
        "collection_key": "spec022-methodological-universe",
        "members": [{"ref": {"asset_key": a["stable_key"]}} for a in ASSETS],
        "title": "Specification 022 controlled methodological universe",
    }],
    "format": "ads-reusable-knowledge-bundle",
    "provenance_sources": [{
        "locator": "docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md",
        "notes": "Prospective benchmark-only synthesis. Not accepted methodological authority.",
        "source_id": SOURCE_ID,
        "source_type": "PROJECT_DESIGN_SYNTHESIS",
        "title": "Specification 022 controlled-universe design synthesis",
        "version_or_fingerprint": None,
    }],
    "relations": RELATIONS,
    "schema_version": 1,
}


def obj(object_id, object_type, title, description, facts=None):
    return {
        "object_id": object_id,
        "object_type": object_type,
        "title": title,
        "description": description,
        "facts": facts or {},
    }


def snap(snapshot_id, transition_summary, project_facts, objects):
    return {
        "snapshot_id": snapshot_id,
        "transition_summary": transition_summary,
        "project_facts": project_facts,
        "objects": objects,
        "relations": [],
    }


e1_base_facts = {
    "project.task.is_supervised_classification": True,
    "project.generalization.is_future_facing": True,
    "project.use.requires_pre_outcome_prediction": True,
    "data.entities.repeat_across_rows": True,
    "data.representation.is_supported_tabular": True,
    "output.probability_used_as_probability": False,
    "deployment.subgroup_reliability_required": False,
}
e1_o1 = obj("E1-O1", "Objective", "Monthly churn risk scoring", "Score active customers at the start of each month so retention actions can be chosen before the following month unfolds.")
e1_o2 = obj("E1-O2", "Dataset", "Customer-month modelling table", "Each row is one customer-month snapshot. The same customer can appear in many months.", {"row_unit": "customer-month", "entity_key": "customer_id"})
e1_o3 = obj("E1-O3", "Question", "Operational scoring cutoff unresolved", "The team has not yet fixed the exact clock-time cutoff that separates information available for scoring from information arriving later.")
e1_s0 = snap("E1-S0", "Initial future-facing churn objective and customer-month structure are known; prediction cutoff and class prevalence are not yet established.", e1_base_facts, [e1_o1, e1_o2, e1_o3])
e1_f1 = dict(e1_base_facts, **{
    "prediction.moment.is_defined": True,
    "target.class_prevalence.is_materially_imbalanced": True,
})
e1_o4 = obj("E1-O4", "Decision", "Prediction moment fixed", "The production score is computed at 00:00 on the first calendar day of each month using only information committed before that cutoff.", {"cutoff": "month-start 00:00"})
e1_o5 = obj("E1-O5", "Finding", "Positive prevalence is 4 percent", "Historical churn prevalence is approximately 4 percent overall and remains between 3 and 5 percent across recent months.", {"positive_prevalence": 0.04})
e1_o6 = obj("E1-O6", "Question", "Feature timing audit pending", "Source-system arrival times have not yet been checked against the newly fixed monthly scoring cutoff.")
e1_s1 = snap("E1-S1", "The prediction moment is now explicit and the target is materially imbalanced; feature timing still requires an audit.", e1_f1, [e1_o1, e1_o2, e1_o4, e1_o5, e1_o6])
e1_f2 = dict(e1_f1, **{
    "data.feature_availability.violation_observed": True,
    "data.leakage.suspected_or_observed": True,
    "target.label_maturity.violation_observed": True,
})
e1_o7 = obj("E1-O7", "Finding", "Three candidate features arrive after scoring", "Three high-ranked behavioural features are populated between two and five days after the month-start scoring cutoff.", {"late_feature_count": 3})
e1_o8 = obj("E1-O8", "Finding", "Recent churn labels lack full follow-up", "Churn is defined as 60 days without activity, but the newest training rows have only 20 days of follow-up before the extraction cutoff.", {"required_followup_days": 60, "available_followup_days": 20})
e1_s2 = snap("E1-S2", "The timing audit found post-cutoff predictors and the current target extraction includes rows without a complete label-observation window.", e1_f2, [e1_o1, e1_o2, e1_o4, e1_o5, e1_o7, e1_o8])

e2_f0 = {
    "project.task.is_supervised_classification": True,
    "project.generalization.is_future_facing": False,
    "project.use.requires_pre_outcome_prediction": True,
    "prediction.moment.is_defined": True,
    "data.entities.repeat_across_rows": False,
    "data.representation.is_supported_tabular": True,
    "output.probability_used_as_probability": False,
    "decision.threshold_required": False,
    "decision.costs_are_asymmetric": False,
    "deployment.subgroup_reliability_required": False,
}
e2_o1 = obj("E2-O1", "Objective", "Static component defect classification", "Predict whether a component will fail its destructive quality test from nondestructive measurements collected immediately beforehand. Deployment is to new independent components, not future calendar periods.")
e2_o2 = obj("E2-O2", "Dataset", "One row per independent component", "Each row is one component and component identifiers do not repeat across rows.", {"row_unit": "component"})
e2_o3 = obj("E2-O3", "Variable", "Inspection date metadata", "A calendar inspection_date column records when the laboratory test occurred, but calendar extrapolation is not part of the deployment claim.")
e2_o4 = obj("E2-O4", "Decision", "Three-way split planned", "The team intends to use separate train, validation, and final test partitions but has not yet frozen the preprocessing workflow.")
e2_s0 = snap("E2-S0", "The task is static tabular classification with independent components and a date-like metadata field that does not imply temporal deployment.", e2_f0, [e2_o1, e2_o2, e2_o3, e2_o4])
e2_f1 = dict(e2_f0, **{"data.leakage.suspected_or_observed": True})
e2_o5 = obj("E2-O5", "Finding", "Imputer and scaler fitted before splitting", "Median imputation and standardization were fitted once on the full dataset before train, validation, and test rows were separated.")
e2_o6 = obj("E2-O6", "Finding", "Label-based feature selection used the full dataset", "A univariate feature screen used the target across all rows before the data split was created.")
e2_s1 = snap("E2-S1", "The initial workflow reveals full-data preprocessing and target-informed feature selection before the split.", e2_f1, [e2_o1, e2_o2, e2_o3, e2_o4, e2_o5, e2_o6])
e2_f2 = dict(e2_f0, **{"data.leakage.suspected_or_observed": False, "final.test.is_locked": True})
e2_o7 = obj("E2-O7", "Decision", "Split-first pipeline correction accepted", "All learned preprocessing and feature selection are now fitted inside training folds. The final test set has been locked away.")
e2_o8 = obj("E2-O8", "Finding", "Logistic baseline established", "A regularized logistic-regression baseline is complete and valid on the validation split.")
e2_o9 = obj("E2-O9", "Finding", "Validation errors suggest nonlinear structure", "Error analysis shows consistent interaction-like residual patterns that the linear baseline does not capture.")
e2_s2 = snap("E2-S2", "Leakage defects are corrected, the final test is locked, and evidence now justifies a compact nonlinear model-family comparison.", e2_f2, [e2_o1, e2_o2, e2_o3, e2_o7, e2_o8, e2_o9])

e3_f0 = {
    "project.task.is_supervised_classification": True,
    "project.generalization.is_future_facing": True,
    "project.use.requires_pre_outcome_prediction": True,
    "prediction.moment.is_defined": True,
    "data.entities.repeat_across_rows": False,
    "data.representation.is_supported_tabular": True,
    "target.class_prevalence.is_materially_imbalanced": True,
    "output.probability_used_as_probability": True,
    "deployment.subgroup_reliability_required": False,
}
e3_o1 = obj("E3-O1", "Objective", "Seven-day equipment failure probability", "Produce a seven-day failure probability for each machine so preventive-maintenance decisions can use estimated risk.")
e3_o2 = obj("E3-O2", "Finding", "Failure prevalence is 8 percent", "The positive event occurs in approximately 8 percent of evaluation windows.", {"positive_prevalence": 0.08})
e3_o3 = obj("E3-O3", "Decision", "Temporal evaluation already established", "A prospectively aligned temporal validation protocol and prediction cutoff were previously reviewed and accepted for this project.")
e3_o4 = obj("E3-O4", "Deliverable", "Probabilities used as operational risks", "Operations will interpret model outputs as numerical failure probabilities, not only as ranking scores.")
e3_s0 = snap("E3-S0", "The project already has a valid temporal evaluation design, and the remaining decision problem requires meaningful failure probabilities.", e3_f0, [e3_o1, e3_o2, e3_o3, e3_o4])
e3_f1 = dict(e3_f0, **{"decision.threshold_required": True, "decision.costs_are_asymmetric": True})
e3_o5 = obj("E3-O5", "Finding", "False negatives are eight times as costly", "Operations estimate the cost of a missed failure at eight times the cost of an unnecessary preventive-maintenance intervention.", {"false_negative_to_false_positive_cost_ratio": 8})
e3_o6 = obj("E3-O6", "Decision", "Decision cutoff must be selected", "A decision rule will be chosen after model comparison using validation evidence rather than a fixed 0.5 cutoff.")
e3_s1 = snap("E3-S1", "The operational error-cost asymmetry and need for a selected decision cutoff are now explicit.", e3_f1, [e3_o1, e3_o2, e3_o3, e3_o4, e3_o5, e3_o6])
e3_f2 = dict(e3_f1, **{"final.test.is_locked": True})
e3_o7 = obj("E3-O7", "Finding", "Candidate models compared on validation data", "The compact model comparison is complete and one probability model is provisionally selected from validation evidence.")
e3_o8 = obj("E3-O8", "Decision", "Final test locked", "The final test partition remains untouched until probability calibration and the operational decision policy are frozen.")
e3_o9 = obj("E3-O9", "Constraint", "Maintenance capacity is exactly 50 machines per day", "Operations can service at most 50 machines each day, so the final action policy must respect a hard daily capacity constraint.", {"daily_capacity": 50})
e3_s2 = snap("E3-S2", "Model comparison is complete, the final test remains locked, and a hard daily intervention-capacity constraint is newly known.", e3_f2, [e3_o1, e3_o2, e3_o3, e3_o4, e3_o5, e3_o6, e3_o7, e3_o8, e3_o9])

e4_f0 = {
    "project.task.is_supervised_classification": True,
    "project.generalization.is_future_facing": False,
    "project.use.requires_pre_outcome_prediction": True,
    "prediction.moment.is_defined": True,
    "data.entities.repeat_across_rows": False,
    "data.representation.is_supported_tabular": True,
    "output.probability_used_as_probability": False,
    "deployment.subgroup_reliability_required": True,
}
e4_o1 = obj("E4-O1", "Objective", "Revalidate an existing multi-site quality model", "Assess whether an existing defect-risk model remains valid after a production data-collection migration across manufacturing sites.")
e4_o2 = obj("E4-O2", "Finding", "Development missingness was 3 percent", "The original development data had approximately 3 percent missing sensor values overall.", {"development_missingness": 0.03})
e4_o3 = obj("E4-O3", "Question", "Production missingness profile not yet measured", "The team has not yet quantified missingness after the collection-system migration.")
e4_o4 = obj("E4-O4", "Definition", "Site is a required reliability subgroup", "The deployment review requires acceptable behaviour separately for sites A, B, and C.")
e4_s0 = snap("E4-S0", "The migration review starts with known historical missingness but no measured post-migration missingness profile.", e4_f0, [e4_o1, e4_o2, e4_o3, e4_o4])
e4_f1 = dict(e4_f0, **{
    "data.production_missingness_profile.is_known": True,
    "data.measurement_regime.changed": True,
    "data.distribution_shift.suspected_or_observed": True,
})
e4_o5 = obj("E4-O5", "Event", "Site B collection system replaced", "Site B moved to a new sensor gateway and ingestion pipeline during the deployment period.")
e4_o6 = obj("E4-O6", "Finding", "Site B missingness increased to 18 percent", "Post-migration Site B records have 18 percent missing sensor values compared with 3 percent in the development data.", {"site_b_missingness": 0.18})
e4_o7 = obj("E4-O7", "Finding", "One sensor changed units", "A temperature field at Site B is now stored in Fahrenheit while the original model pipeline assumes Celsius.")
e4_s1 = snap("E4-S1", "Post-migration evidence shows a measurement-regime change, a large missingness shift, and a unit mismatch at Site B.", e4_f1, [e4_o1, e4_o2, e4_o4, e4_o5, e4_o6, e4_o7])
e4_f2 = dict(e4_f0, **{
    "data.production_missingness_profile.is_known": True,
    "data.measurement_regime.changed": False,
    "data.distribution_shift.suspected_or_observed": True,
})
e4_o8 = obj("E4-O8", "Decision", "Unit conversion and missingness pipeline repaired", "The Site B unit conversion is corrected and the missingness-handling pipeline now matches the observed production pattern.")
e4_o9 = obj("E4-O9", "Finding", "Site B validation performance remains degraded", "After the data-pipeline repair, Site B error remains materially worse than Sites A and C on the current revalidation sample.")
e4_o10 = obj("E4-O10", "Question", "Model revalidation remains unresolved", "The team has not yet decided whether the repaired data pipeline is sufficient or whether the model itself must be updated.")
e4_s2 = snap("E4-S2", "The immediate measurement and missingness defects are repaired, but subgroup performance remains degraded and revalidation is still unresolved.", e4_f2, [e4_o1, e4_o2, e4_o4, e4_o8, e4_o9, e4_o10])

EPISODES = {
    "schema_version": 1,
    "benchmark_id": "spec022-project-state-episodes-v1",
    "episodes": [
        {"episode_id": "E1", "title": "Future binary prediction", "snapshots": [e1_s0, e1_s1, e1_s2]},
        {"episode_id": "E2", "title": "Static tabular prediction without temporal deployment", "snapshots": [e2_s0, e2_s1, e2_s2]},
        {"episode_id": "E3", "title": "Probability-sensitive decision problem", "snapshots": [e3_s0, e3_s1, e3_s2]},
        {"episode_id": "E4", "title": "Data-quality and measurement shift", "snapshots": [e4_s0, e4_s1, e4_s2]},
    ],
}


def oracle_item(oracle_id, episode_id, concern, importance, aliases, states, grounding, rationale, missing_question=None):
    return {
        "oracle_id": oracle_id,
        "episode_id": episode_id,
        "canonical_concern": concern,
        "importance_class": importance,
        "acceptable_aliases": aliases,
        "state_by_snapshot": states,
        "grounding_project_object_ids_by_snapshot": grounding,
        "missing_context_question_semantics": missing_question,
        "rationale": rationale,
    }


ORACLE_ITEMS = [
    oracle_item("E1-C01", "E1", "define the operational prediction moment", "CRITICAL_VALIDITY", ["define the scoring cutoff", "fix the prediction cutoff"], {"E1-S0": "ACTIVE", "E1-S1": "RESOLVED", "E1-S2": "RESOLVED"}, {"E1-S0": ["E1-O1", "E1-O3"], "E1-S1": ["E1-O4"], "E1-S2": ["E1-O4"]}, "Future-facing scoring cannot be evaluated or feature-timed rigorously until the operational cutoff is explicit."),
    oracle_item("E1-C02", "E1", "verify prediction-time feature eligibility", "CRITICAL_VALIDITY", ["audit feature availability at scoring time", "check whether predictors exist before scoring"], {"E1-S0": "MISSING_CONTEXT", "E1-S1": "ACTIVE", "E1-S2": "ACTIVE"}, {"E1-S0": ["E1-O3"], "E1-S1": ["E1-O4", "E1-O6"], "E1-S2": ["E1-O4", "E1-O7"]}, "Features unavailable by the scoring cutoff invalidate deployment-facing model evidence.", "What exact scoring cutoff determines whether each candidate feature is available for prediction?"),
    oracle_item("E1-C03", "E1", "use temporal validation aligned with future deployment", "CRITICAL_VALIDITY", ["chronological validation", "past-to-future validation"], {"E1-S0": "MISSING_CONTEXT", "E1-S1": "ACTIVE", "E1-S2": "ACTIVE"}, {"E1-S0": ["E1-O1", "E1-O3"], "E1-S1": ["E1-O1", "E1-O4"], "E1-S2": ["E1-O1", "E1-O4"]}, "A future deployment claim requires validation that respects the temporal information boundary.", "What exact prediction cutoff and deployment cadence should the validation splits reproduce?"),
    oracle_item("E1-C04", "E1", "account for repeated-customer generalization", "HIGH_VALUE", ["repeated-entity generalization", "customer-level generalization"], {"E1-S0": "ACTIVE", "E1-S1": "ACTIVE", "E1-S2": "ACTIVE"}, {"E1-S0": ["E1-O2"], "E1-S1": ["E1-O2"], "E1-S2": ["E1-O2"]}, "Repeated customer-month rows create a generalization choice that must match the intended deployment claim."),
    oracle_item("E1-C05", "E1", "use entity-aware splitting when repeated customers would cross folds", "HIGH_VALUE", ["group-aware validation", "customer-group split"], {"E1-S0": "ACTIVE", "E1-S1": "ACTIVE", "E1-S2": "ACTIVE"}, {"E1-S0": ["E1-O2"], "E1-S1": ["E1-O2"], "E1-S2": ["E1-O2"]}, "Repeated entities can make ordinary random row splits optimistic when entity independence is required."),
    oracle_item("E1-C06", "E1", "measure and account for class imbalance", "HIGH_VALUE", ["inspect positive prevalence", "class-prevalence imbalance"], {"E1-S0": "MISSING_CONTEXT", "E1-S1": "ACTIVE", "E1-S2": "ACTIVE"}, {"E1-S0": ["E1-O1"], "E1-S1": ["E1-O5"], "E1-S2": ["E1-O5"]}, "The evaluation regime depends on whether the positive class is materially rare.", "What is the positive-class prevalence overall and across recent deployment-relevant periods?"),
    oracle_item("E1-C07", "E1", "use minority-sensitive classification metrics", "HIGH_VALUE", ["precision recall metrics", "minority-class evaluation"], {"E1-S0": "MISSING_CONTEXT", "E1-S1": "ACTIVE", "E1-S2": "ACTIVE"}, {"E1-S0": ["E1-O1"], "E1-S1": ["E1-O5"], "E1-S2": ["E1-O5"]}, "A four-percent positive class makes accuracy alone insufficient for judging useful performance.", "What is the positive-class prevalence and which minority errors matter operationally?"),
    oracle_item("E1-C08", "E1", "prevent future or post-cutoff information leakage", "CRITICAL_VALIDITY", ["temporal leakage", "look-ahead leakage"], {"E1-S0": "MISSING_CONTEXT", "E1-S1": "ACTIVE", "E1-S2": "ACTIVE"}, {"E1-S0": ["E1-O3"], "E1-S1": ["E1-O4", "E1-O6"], "E1-S2": ["E1-O7"]}, "Future-facing evidence is invalid if post-cutoff information reaches training features or evaluation.", "What information boundary separates facts known at scoring from facts observed afterward?"),
    oracle_item("E1-C09", "E1", "ensure every training label has a complete outcome-observation window", "CRITICAL_VALIDITY", ["label maturity", "complete follow-up window", "target censoring window"], {"E1-S0": "INACTIVE", "E1-S1": "INACTIVE", "E1-S2": "ACTIVE"}, {"E1-S2": ["E1-O8"]}, "Recent rows without the full sixty-day label window can create systematically immature or censored targets."),

    oracle_item("E2-C01", "E2", "separate train validation and final test roles", "CRITICAL_VALIDITY", ["three-way split", "train validation test separation"], {"E2-S0": "ACTIVE", "E2-S1": "ACTIVE", "E2-S2": "RESOLVED"}, {"E2-S0": ["E2-O4"], "E2-S1": ["E2-O4", "E2-O5", "E2-O6"], "E2-S2": ["E2-O7"]}, "Adaptive model development requires distinct fitting, selection, and final-evaluation data roles."),
    oracle_item("E2-C02", "E2", "protect the final test set from iterative selection", "HIGH_VALUE", ["lock the test set", "final-test protection"], {"E2-S0": "ACTIVE", "E2-S1": "ACTIVE", "E2-S2": "RESOLVED"}, {"E2-S0": ["E2-O4"], "E2-S1": ["E2-O4"], "E2-S2": ["E2-O7"]}, "The final test must remain untouched until adaptive modelling choices are complete."),
    oracle_item("E2-C03", "E2", "fit learned preprocessing only inside training data", "CRITICAL_VALIDITY", ["preprocessing fit isolation", "fit imputation and scaling on training folds"], {"E2-S0": "ACTIVE", "E2-S1": "ACTIVE", "E2-S2": "RESOLVED"}, {"E2-S0": ["E2-O4"], "E2-S1": ["E2-O5"], "E2-S2": ["E2-O7"]}, "Full-data preprocessing leaks validation and test distribution information into the fitted pipeline."),
    oracle_item("E2-C04", "E2", "perform feature selection inside the evaluation procedure", "CRITICAL_VALIDITY", ["feature selection isolation", "nested feature selection"], {"E2-S0": "INACTIVE", "E2-S1": "ACTIVE", "E2-S2": "RESOLVED"}, {"E2-S1": ["E2-O6"], "E2-S2": ["E2-O7"]}, "Target-informed feature selection before splitting leaks outcome information into evaluation."),
    oracle_item("E2-C05", "E2", "eliminate data leakage from the modelling workflow", "CRITICAL_VALIDITY", ["data leakage", "full-data leakage"], {"E2-S0": "INACTIVE", "E2-S1": "ACTIVE", "E2-S2": "RESOLVED"}, {"E2-S1": ["E2-O5", "E2-O6"], "E2-S2": ["E2-O7"]}, "The discovered preprocessing and feature-selection workflow contaminates evaluation."),
    oracle_item("E2-C06", "E2", "establish a transparent logistic-regression baseline", "HIGH_VALUE", ["linear logistic baseline", "simple classification baseline"], {"E2-S0": "ACTIVE", "E2-S1": "ACTIVE", "E2-S2": "RESOLVED"}, {"E2-S0": ["E2-O1"], "E2-S1": ["E2-O1"], "E2-S2": ["E2-O8"]}, "A transparent baseline anchors the value of additional model complexity."),
    oracle_item("E2-C07", "E2", "compare a compact nonlinear model family after the baseline", "HIGH_VALUE", ["nonlinear model comparison", "compare flexible tabular models"], {"E2-S0": "INACTIVE", "E2-S1": "INACTIVE", "E2-S2": "ACTIVE"}, {"E2-S2": ["E2-O8", "E2-O9"]}, "Observed validation error structure now gives a project-specific reason to test nonlinear alternatives."),
    oracle_item("E2-C08", "E2", "separate adaptive selection from final evaluation", "CRITICAL_VALIDITY", ["selection evaluation separation", "choose on validation and evaluate on test"], {"E2-S0": "ACTIVE", "E2-S1": "ACTIVE", "E2-S2": "ACTIVE"}, {"E2-S0": ["E2-O4"], "E2-S1": ["E2-O4"], "E2-S2": ["E2-O7", "E2-O9"]}, "Model and workflow choices must be made with validation evidence rather than final-test feedback."),

    oracle_item("E3-C01", "E3", "assess probability calibration", "HIGH_VALUE", ["calibration", "reliability of predicted probabilities"], {"E3-S0": "ACTIVE", "E3-S1": "ACTIVE", "E3-S2": "ACTIVE"}, {"E3-S0": ["E3-O1", "E3-O4"], "E3-S1": ["E3-O1", "E3-O4"], "E3-S2": ["E3-O1", "E3-O4"]}, "Operational use of numerical risk requires probability estimates that correspond to observed frequencies."),
    oracle_item("E3-C02", "E3", "evaluate probabilities with proper scoring rules", "HIGH_VALUE", ["log loss or Brier score", "proper probability scoring"], {"E3-S0": "ACTIVE", "E3-S1": "ACTIVE", "E3-S2": "ACTIVE"}, {"E3-S0": ["E3-O4"], "E3-S1": ["E3-O4"], "E3-S2": ["E3-O4"]}, "Ranking metrics alone do not evaluate the quality of full probability forecasts."),
    oracle_item("E3-C03", "E3", "account for class imbalance", "HIGH_VALUE", ["rare-event prevalence", "class imbalance"], {"E3-S0": "ACTIVE", "E3-S1": "ACTIVE", "E3-S2": "ACTIVE"}, {"E3-S0": ["E3-O2"], "E3-S1": ["E3-O2"], "E3-S2": ["E3-O2"]}, "An eight-percent event rate affects interpretation of classification evidence."),
    oracle_item("E3-C04", "E3", "use minority-sensitive classification metrics", "HIGH_VALUE", ["precision recall evaluation", "minority-sensitive metrics"], {"E3-S0": "ACTIVE", "E3-S1": "ACTIVE", "E3-S2": "ACTIVE"}, {"E3-S0": ["E3-O2"], "E3-S1": ["E3-O2"], "E3-S2": ["E3-O2"]}, "Rare failures require evidence that exposes positive-class errors in addition to probability quality."),
    oracle_item("E3-C05", "E3", "represent asymmetric false-positive and false-negative costs", "HIGH_VALUE", ["asymmetric error costs", "false-negative cost"], {"E3-S0": "MISSING_CONTEXT", "E3-S1": "ACTIVE", "E3-S2": "ACTIVE"}, {"E3-S0": ["E3-O1"], "E3-S1": ["E3-O5"], "E3-S2": ["E3-O5"]}, "The operational decision rule depends on the relative consequences of intervention and missed failure.", "What are the operational costs or utilities of false positives and false negatives?"),
    oracle_item("E3-C06", "E3", "select the operational decision threshold from validation evidence", "HIGH_VALUE", ["threshold selection", "choose the operating cutoff"], {"E3-S0": "MISSING_CONTEXT", "E3-S1": "ACTIVE", "E3-S2": "ACTIVE"}, {"E3-S0": ["E3-O1"], "E3-S1": ["E3-O6"], "E3-S2": ["E3-O6", "E3-O9"]}, "A hard decision cutoff should follow the operational objective rather than default to 0.5.", "Will operations use a hard decision cutoff, ranking policy, or another constrained action rule?"),
    oracle_item("E3-C07", "E3", "keep policy selection separate from final evaluation", "CRITICAL_VALIDITY", ["selection evaluation separation", "choose calibration and threshold on validation"], {"E3-S0": "ACTIVE", "E3-S1": "ACTIVE", "E3-S2": "ACTIVE"}, {"E3-S0": ["E3-O4"], "E3-S1": ["E3-O6"], "E3-S2": ["E3-O7", "E3-O8"]}, "Calibration and decision-policy choices are adaptive and must be frozen before final testing."),
    oracle_item("E3-C08", "E3", "protect the final test set", "CRITICAL_VALIDITY", ["final-test protection", "keep test locked"], {"E3-S0": "ACTIVE", "E3-S1": "ACTIVE", "E3-S2": "RESOLVED"}, {"E3-S0": ["E3-O4"], "E3-S1": ["E3-O6"], "E3-S2": ["E3-O8"]}, "The final test must not be used to tune calibration or the action policy."),
    oracle_item("E3-C09", "E3", "temporal validation for future deployment", "HIGH_VALUE", ["temporal validation", "future-aligned validation"], {"E3-S0": "RESOLVED", "E3-S1": "RESOLVED", "E3-S2": "RESOLVED"}, {"E3-S0": ["E3-O3"], "E3-S1": ["E3-O3"], "E3-S2": ["E3-O3"]}, "Temporal validation remains methodologically relevant but is already resolved and should not persist as current work."),
    oracle_item("E3-C10", "E3", "choose an action policy that respects the hard daily intervention capacity", "HIGH_VALUE", ["capacity-constrained decision policy", "top-k policy under fixed capacity"], {"E3-S0": "INACTIVE", "E3-S1": "INACTIVE", "E3-S2": "ACTIVE"}, {"E3-S2": ["E3-O9"]}, "A fixed service capacity can make a simple unconstrained threshold an incomplete operational policy."),

    oracle_item("E4-C01", "E4", "characterize missingness in the current data", "HIGH_VALUE", ["missingness characterization", "missing-data profile"], {"E4-S0": "ACTIVE", "E4-S1": "ACTIVE", "E4-S2": "RESOLVED"}, {"E4-S0": ["E4-O2", "E4-O3"], "E4-S1": ["E4-O2", "E4-O6"], "E4-S2": ["E4-O8"]}, "Missingness is itself part of the changed data-generating and measurement process."),
    oracle_item("E4-C02", "E4", "compare production missingness with development missingness", "CRITICAL_VALIDITY", ["production missingness alignment", "missingness shift"], {"E4-S0": "MISSING_CONTEXT", "E4-S1": "ACTIVE", "E4-S2": "RESOLVED"}, {"E4-S0": ["E4-O2", "E4-O3"], "E4-S1": ["E4-O2", "E4-O6"], "E4-S2": ["E4-O8"]}, "Deployment validity depends on whether missingness patterns changed after migration.", "What are the post-migration missingness rates overall and by site for the variables used by the model?"),
    oracle_item("E4-C03", "E4", "evaluate subgroup robustness by site", "HIGH_VALUE", ["site-level robustness", "subgroup performance"], {"E4-S0": "ACTIVE", "E4-S1": "ACTIVE", "E4-S2": "ACTIVE"}, {"E4-S0": ["E4-O4"], "E4-S1": ["E4-O4", "E4-O6"], "E4-S2": ["E4-O4", "E4-O9"]}, "Aggregate performance can hide a deployment failure isolated to one required site subgroup."),
    oracle_item("E4-C04", "E4", "reassess comparability after the measurement-regime change", "CRITICAL_VALIDITY", ["measurement-regime change", "sensor unit change"], {"E4-S0": "INACTIVE", "E4-S1": "ACTIVE", "E4-S2": "RESOLVED"}, {"E4-S1": ["E4-O5", "E4-O7"], "E4-S2": ["E4-O8"]}, "Changed collection systems and units can invalidate the meaning and scale of model inputs."),
    oracle_item("E4-C05", "E4", "assess distribution shift after the collection migration", "HIGH_VALUE", ["distribution shift", "data drift after migration"], {"E4-S0": "MISSING_CONTEXT", "E4-S1": "ACTIVE", "E4-S2": "ACTIVE"}, {"E4-S0": ["E4-O1", "E4-O3"], "E4-S1": ["E4-O5", "E4-O6", "E4-O7"], "E4-S2": ["E4-O9"]}, "Post-migration data may differ materially from the development distribution even after obvious pipeline defects are repaired.", "What post-migration feature distributions are observed overall and by site relative to the development data?"),
    oracle_item("E4-C06", "E4", "revalidate the model after material data changes", "CRITICAL_VALIDITY", ["model revalidation", "revalidate after data change"], {"E4-S0": "INACTIVE", "E4-S1": "ACTIVE", "E4-S2": "ACTIVE"}, {"E4-S1": ["E4-O5", "E4-O6", "E4-O7"], "E4-S2": ["E4-O9", "E4-O10"]}, "Material measurement and distribution changes can invalidate prior model evidence and require fresh validation."),
]

INACTIVE_CONTROLS = {
    "E1-S0": ["probability-calibration", "threshold-selection", "measurement-regime-change"],
    "E1-S1": ["probability-calibration", "threshold-selection", "measurement-regime-change"],
    "E1-S2": ["probability-calibration", "threshold-selection", "measurement-regime-change"],
    "E2-S0": ["temporal-validation", "temporal-leakage", "repeated-entity-generalization", "group-aware-validation"],
    "E2-S1": ["temporal-validation", "temporal-leakage", "repeated-entity-generalization", "group-aware-validation"],
    "E2-S2": ["temporal-validation", "temporal-leakage", "repeated-entity-generalization", "group-aware-validation"],
    "E3-S0": ["measurement-regime-change", "distribution-shift", "subgroup-robustness"],
    "E3-S1": ["measurement-regime-change", "distribution-shift", "subgroup-robustness"],
    "E3-S2": ["measurement-regime-change", "distribution-shift", "subgroup-robustness"],
    "E4-S0": ["probability-calibration", "threshold-selection", "temporal-validation"],
    "E4-S1": ["probability-calibration", "threshold-selection", "temporal-validation"],
    "E4-S2": ["probability-calibration", "threshold-selection", "temporal-validation"],
}

ORACLE = {
    "schema_version": 1,
    "benchmark_id": "spec022-coverage-oracle-v1",
    "importance_weights": {"CRITICAL_VALIDITY": 4, "HIGH_VALUE": 2, "USEFUL": 1, "OPTIONAL": 0},
    "default_unspecified_state": "INACTIVE",
    "items": ORACLE_ITEMS,
    "inactive_controls_by_snapshot": INACTIVE_CONTROLS,
}

MAP = {
    "schema_version": 1,
    "benchmark_id": "spec022-oracle-representation-map-v1",
    "mappings": [
        {"oracle_id": "E1-C01", "stable_keys": ["prediction-moment"]},
        {"oracle_id": "E1-C02", "stable_keys": ["prediction-time-feature-eligibility"]},
        {"oracle_id": "E1-C03", "stable_keys": ["temporal-validation"]},
        {"oracle_id": "E1-C04", "stable_keys": ["repeated-entity-generalization"]},
        {"oracle_id": "E1-C05", "stable_keys": ["group-aware-validation"]},
        {"oracle_id": "E1-C06", "stable_keys": ["class-imbalance"]},
        {"oracle_id": "E1-C07", "stable_keys": ["minority-sensitive-metrics"]},
        {"oracle_id": "E1-C08", "stable_keys": ["temporal-leakage", "data-leakage"]},
        {"oracle_id": "E1-C09", "stable_keys": []},
        {"oracle_id": "E2-C01", "stable_keys": ["train-validation-test-separation"]},
        {"oracle_id": "E2-C02", "stable_keys": ["final-test-protection"]},
        {"oracle_id": "E2-C03", "stable_keys": ["preprocessing-fit-isolation"]},
        {"oracle_id": "E2-C04", "stable_keys": ["feature-selection-isolation"]},
        {"oracle_id": "E2-C05", "stable_keys": ["data-leakage"]},
        {"oracle_id": "E2-C06", "stable_keys": ["linear-logistic-baseline"]},
        {"oracle_id": "E2-C07", "stable_keys": ["nonlinear-model-comparison"]},
        {"oracle_id": "E2-C08", "stable_keys": ["selection-evaluation-separation"]},
        {"oracle_id": "E3-C01", "stable_keys": ["probability-calibration"]},
        {"oracle_id": "E3-C02", "stable_keys": ["proper-scoring-rules"]},
        {"oracle_id": "E3-C03", "stable_keys": ["class-imbalance"]},
        {"oracle_id": "E3-C04", "stable_keys": ["minority-sensitive-metrics"]},
        {"oracle_id": "E3-C05", "stable_keys": ["asymmetric-error-costs"]},
        {"oracle_id": "E3-C06", "stable_keys": ["threshold-selection"]},
        {"oracle_id": "E3-C07", "stable_keys": ["selection-evaluation-separation"]},
        {"oracle_id": "E3-C08", "stable_keys": ["final-test-protection"]},
        {"oracle_id": "E3-C09", "stable_keys": ["temporal-validation"]},
        {"oracle_id": "E3-C10", "stable_keys": []},
        {"oracle_id": "E4-C01", "stable_keys": ["missing-data"]},
        {"oracle_id": "E4-C02", "stable_keys": ["production-missingness-alignment"]},
        {"oracle_id": "E4-C03", "stable_keys": ["subgroup-robustness"]},
        {"oracle_id": "E4-C04", "stable_keys": ["measurement-regime-change"]},
        {"oracle_id": "E4-C05", "stable_keys": ["distribution-shift"]},
        {"oracle_id": "E4-C06", "stable_keys": ["revalidation-after-data-change"]},
    ],
}

FILES = {
    "spec022_methodological_universe_v1.json": UNIVERSE,
    "spec022_project_state_episodes_v1.json": EPISODES,
    "spec022_coverage_oracle_v1.json": ORACLE,
    "spec022_oracle_representation_map_v1.json": MAP,
}


def canonical_bytes(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


manifest = {
    "schema_version": 1,
    "benchmark_id": "spec022-contract-fixture-manifest-v1",
    "files": {},
}
for name, value in FILES.items():
    text = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    (OUT / name).write_text(text, encoding="utf-8")
    manifest["files"][name] = {
        "canonical_sha256": hashlib.sha256(canonical_bytes(value)).hexdigest(),
        "canonical_bytes": len(canonical_bytes(value)),
    }

(OUT / "spec022_contract_fixture_manifest_v1.json").write_text(
    json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

print(f"assets={len(ASSETS)}")
print(f"relations={len(RELATIONS)}")
print(f"episodes={len(EPISODES['episodes'])}")
print(f"snapshots={sum(len(e['snapshots']) for e in EPISODES['episodes'])}")
print(f"oracle_items={len(ORACLE_ITEMS)}")
print(f"catalog_gaps={sum(1 for m in MAP['mappings'] if not m['stable_keys'])}")
