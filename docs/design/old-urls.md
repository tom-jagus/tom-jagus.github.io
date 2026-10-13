# Old URL inventory

This inventory records the tracked legacy HTML and RSS output at commit `4292a286e97648002a9c261fe3a24c207ce1160f`, before repository cleanup. It is evidence of stored output, not a check of live routes, traffic, or incoming links.

There were 47 HTML routes and 12 RSS routes. Decide which old links are useful before launch. No redirects or aliases were added during cleanup.

## Paths kept by the rewrite

- `/`
- `/about/`
- `/contact/`
- `/services/`

The separate pages are currently drafts. Keeping their intended paths does not mean they are already published.

## Old collections and generated navigation

```text
/authors/
/blog/
/blog/page/1/
/categories/
/page/1/
/series/
/services/page/1/
/tags/
```

Review whether `/blog/` should lead to `/writing/` once it has launch content. Taxonomy and pagination routes do not have automatic replacements. Do not redirect unrelated pages to Home merely to avoid a 404.

## Old service pages

These are the former service categories and write-ups. The new Services page uses the five current brand offers instead. Any useful links need a reviewed destination, potentially a matching section on `/services/`.

```text
/services/advisory_and_enablement/
/services/advisory_and_enablement/internal_tooling_strategy/
/services/advisory_and_enablement/knowledge_base_development/
/services/advisory_and_enablement/page/1/
/services/advisory_and_enablement/process_improvement_consulting/
/services/advisory_and_enablement/team_onboarding_and_workflow_design/
/services/advisory_and_enablement/technical_mentorship/
/services/architecture_and_system_design/
/services/architecture_and_system_design/data_and_reporting_infrastructure_planning/
/services/architecture_and_system_design/governance_and_documentation_patterns/
/services/architecture_and_system_design/page/1/
/services/architecture_and_system_design/reusability_and_modularization_strategy/
/services/architecture_and_system_design/solution_architecture/
/services/architecture_and_system_design/toolchain_evaluation_and_integration/
/services/data_engineering_and_automation/
/services/data_engineering_and_automation/api_integration_and_scripting/
/services/data_engineering_and_automation/data_pipeline_design/
/services/data_engineering_and_automation/data_transformation_workflows/
/services/data_engineering_and_automation/etl_elt_automation/
/services/data_engineering_and_automation/metadata_driven_automation/
/services/data_engineering_and_automation/page/1/
/services/llms_and_ai_workflows/
/services/llms_and_ai_workflows/embedding_based_search_and_retrieval/
/services/llms_and_ai_workflows/generative_ai_integration/
/services/llms_and_ai_workflows/intelligent_assistant_and_prototype_design/
/services/llms_and_ai_workflows/llm_powered_automation/
/services/llms_and_ai_workflows/page/1/
/services/llms_and_ai_workflows/prompt_engineering_and_tuning/
/services/reporting_and_analytics/
/services/reporting_and_analytics/analytics_process_optimization/
/services/reporting_and_analytics/page/1/
/services/reporting_and_analytics/power_bi_model_development/
/services/reporting_and_analytics/report_performance_tuning/
/services/reporting_and_analytics/self_service_reporting_enablement/
/services/reporting_and_analytics/semantic_layer_design/
```

## Old RSS feeds

```text
/authors/index.xml
/blog/index.xml
/categories/index.xml
/index.xml
/series/index.xml
/services/advisory_and_enablement/index.xml
/services/architecture_and_system_design/index.xml
/services/data_engineering_and_automation/index.xml
/services/index.xml
/services/llms_and_ai_workflows/index.xml
/services/reporting_and_analytics/index.xml
/tags/index.xml
```

The new general feed retains `/index.xml`. Section feeds are not configured. Review old subscribers before deciding whether other feed URLs need replacements.

## Historical content and design recovery

All 43 files in the removed `legacy-content/` archive matched the original `content/` tree at the commit above. The original content and generated output remain in Git history. To recover the content without changing the working tree or index:

```bash
mkdir -p /tmp/website-legacy-recovery
git archive 4292a286e97648002a9c261fe3a24c207ce1160f content \
  | tar -x -C /tmp/website-legacy-recovery
```

The untracked static design preview was backed up separately, including all 12 files, before removal. The verified local archive is:

```text
/home/tom/.local/share/website-rewrite-backups/website-cleanup-bK3944n1/design-preview.tar.gz
```

That backup is outside the repository and is not a build dependency. The retained wordmark, avatar, backgrounds, fonts, and font license matched their preview copies byte-for-byte. See [asset sources](assets.md).
