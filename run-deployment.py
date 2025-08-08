from __future__ import annotations

from prefect.deployments import run_deployment

run_deployment(
    name="end-of-run-workflow/tst-workflow-prefect3-deploy",
    # name="end-of-run-workflow/end_of_run_workflow_deployment",
    parameters={"stop_doc": {"run_start": "d106586f-44e6-4045-8bf6-985cfdef3574"}},
    timeout=15,  # don't wait for the run to finish # edit to 15 sec
)
