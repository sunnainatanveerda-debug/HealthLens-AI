
import streamlit as st




st.set_page_config(
    page_title="HealthLens AI",
    page_icon="🔬",
    layout="wide"
)

# Professional visual design
st.markdown("""
<style>
    .stApp {
        background-color: #f5f7fb;
    }

    h1 {
        color: #17365d;
        font-weight: 750;
    }

    h2, h3 {
        color: #245b78;
    }

    div[data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #dce5ef;
        padding: 18px;
        border-radius: 12px;
    }

    div.stButton > button,
    div.stFormSubmitButton > button {
        background-color: #176b87;
        color: white;
        border-radius: 9px;
        border: none;
        padding: 10px 18px;
    }

    div.stFormSubmitButton > button:hover {
        background-color: #124d65;
        color: white;
    }

    section[data-testid="stSidebar"] {
        background-color: #eaf0f8;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🔬 HealthLens AI")
    st.caption("Health education assistant")

    st.markdown("---")
    st.markdown("### Navigation")
    st.markdown("🏠 Home")
    st.markdown("🧪 Result Checker")
    st.markdown("📚 Educational Examples")

    st.markdown("---")
    st.caption("Prototype version 1.0")


# Demo data is fictional and intended only for software testing.
DEMO_CASES = {
    "Choose a demo case": {
        "test": "Hemoglobin",
        "result": 12.0,
        "unit": "g/dL",
        "lower": 12.0,
        "upper": 16.0,
    },
    "Example A — Within supplied range": {
        "test": "Hemoglobin",
        "result": 14.0,
        "unit": "g/dL",
        "lower": 12.0,
        "upper": 16.0,
    },
    "Example B — Below supplied range": {
        "test": "Hemoglobin",
        "result": 10.0,
        "unit": "g/dL",
        "lower": 12.0,
        "upper": 16.0,
    },
    "Example C — Above supplied range": {
        "test": "Glucose",
        "result": 130.0,
        "unit": "mg/dL",
        "lower": 70.0,
        "upper": 99.0,
    },
}


def load_demo():
    """Fill the form when a demo case is selected."""
    case = DEMO_CASES[st.session_state.demo_choice]

    st.session_state.test_name = case["test"]
    st.session_state.result = case["result"]
    st.session_state.unit = case["unit"]
    st.session_state.lower = case["lower"]
    st.session_state.upper = case["upper"]


# Initialize the form values.
defaults = {
    "test_name": "Hemoglobin",
    "result": 12.0,
    "unit": "g/dL",
    "lower": 12.0,
    "upper": 16.0,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

if "demo_choice" not in st.session_state:
    st.session_state.demo_choice = "Choose a demo case"


# App heading
st.title("🔬 HealthLens AI")
st.subheader("Understand laboratory results in simple language")

st.warning(
    "Educational prototype only. This app does not diagnose diseases "
    "or replace advice from a qualified healthcare professional."
)

st.markdown("### 🧭 Explore Demo Cases")

st.write(
    "Select a fictional example to automatically fill the form below."
)

st.selectbox(
    "Choose an example",
    list(DEMO_CASES.keys()),
    key="demo_choice",
    on_change=load_demo,
)

st.caption(
    "All demo values and reference limits are illustrative. "
    "They are not universal medical ranges."
)

st.divider()

# Laboratory result form
st.markdown("### 🧪 Laboratory Result Checker")

with st.form("lab_result_form"):
    st.selectbox(
        "Laboratory test",
        ["Hemoglobin", "Glucose", "Vitamin D"],
        key="test_name",
    )

    st.number_input(
        "Result value",
        min_value=0.0,
        max_value=100000.0,
        step=0.1,
        key="result",
    )

    st.text_input(
        "Unit shown on the report",
        key="unit",
    )

    st.number_input(
        "Lower reference limit",
        min_value=0.0,
        max_value=100000.0,
        step=0.1,
        key="lower",
    )

    st.number_input(
        "Upper reference limit",
        min_value=0.0,
        max_value=100000.0,
        step=0.1,
        key="upper",
    )

    submitted = st.form_submit_button("Understand My Result")


# Display the comparison
if submitted:
    test = st.session_state.test_name
    result = st.session_state.result
    unit = st.session_state.unit.strip()
    lower = st.session_state.lower
    upper = st.session_state.upper

    if not unit:
        st.error("Please enter the unit shown on the report.")

    elif lower > upper:
        st.error("The lower limit cannot exceed the upper limit.")

    else:
        st.markdown("### 📋 Your Result Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Entered result", f"{result:g} {unit}")

        with col2:
            st.write(f"**Test:** {test}")
            st.write(
                f"**Supplied range:** {lower:g}–{upper:g} {unit}"
            )

        if result < lower:
            st.info(
                "Below the supplied reference range. This comparison "
                "cannot identify a cause or establish a diagnosis."
            )

        elif result > upper:
            st.info(
                "Above the supplied reference range. This comparison "
                "cannot identify a cause or establish a diagnosis."
            )

        else:
            st.success(
                "Within the supplied reference range. This alone "
                "does not establish that a person is healthy."
            )

        st.markdown("### 💬 Questions for Your Clinician")

        st.write(
            "- What does this result mean in my personal situation?"
        )
        st.write(
            "- Could symptoms, medicines, or other results affect interpretation?"
        )
        st.write(
            "- Is any follow-up needed?"
        )

        st.caption(
            "Use the reference range and units from the actual laboratory "
            "report. Seek professional medical advice when needed."
        )
        
        # Create a downloadable educational summary
        if result < lower:
            comparison = "Below the supplied reference range"
        elif result > upper:
            comparison = "Above the supplied reference range"
        else:
            comparison = "Within the supplied reference range"

        report_text = f"""
HEALTHLENS AI
Educational Laboratory Result Summary

Test: {test}
Entered result: {result:g} {unit}
Supplied reference range: {lower:g}–{upper:g} {unit}

Comparison: {comparison}

IMPORTANT LIMITATIONS
This report compares your entered result with the supplied range.
It does not diagnose a disease or establish that you are healthy.
Reference ranges and interpretation may vary between laboratories
and individuals.

QUESTIONS FOR YOUR CLINICIAN
1. What does this result mean in my situation?
2. Could symptoms, medicines, or other results affect interpretation?
3. Is follow-up testing appropriate?

HealthLens AI is an educational prototype, not a medical device.
"""

        st.download_button(
            label="📥 Download Result Summary",
            data=report_text,
            file_name="healthlens_result_summary.txt",
            mime="text/plain",
        )

# Health Education Library
st.divider()
st.markdown("## 📚 Health Education Library")

st.write(
    "Learn basic concepts about laboratory testing. "
    "This information is educational and does not interpret "
    "your personal medical condition."
)

with st.expander("1. What is a laboratory reference range?"):
    st.write(
        "A reference range is a range of results that a laboratory "
        "uses as a comparison for a particular test. It may depend "
        "on the laboratory method and the population being studied."
    )
    st.info(
        "Always compare a result with the range and units printed "
        "on the original laboratory report."
    )

with st.expander("2. Does an out-of-range result mean disease?"):
    st.write(
        "Not necessarily. A result outside a reference range does "
        "not automatically establish a disease. A clinician may "
        "consider symptoms, medical history, medicines, and other "
        "test results."
    )

with st.expander("3. Can an in-range result guarantee good health?"):
    st.write(
        "No. A result within a reference range does not rule out "
        "every health problem. The meaning of a result depends on "
        "the person and the clinical context."
    )

with st.expander("4. How should I prepare for a medical appointment?"):
    st.write(
        "- Bring your original laboratory report."
    )
    st.write(
        "- Ask what the result means in your situation."
    )
    st.write(
        "- Tell your clinician about relevant symptoms and medicines."
    )
    st.write(
        "- Ask whether follow-up testing is appropriate."
    )

st.markdown("### 🔎 Trusted Learning Resources")

st.markdown(
    "- [MedlinePlus — Laboratory Tests]"
    "(https://medlineplus.gov/lab-tests/)"
)

st.markdown(
    "- [MedlinePlus — Understanding Your Lab Results]"
    "(https://medlineplus.gov/lab-tests/"
    "understanding-your-lab-test-results/)"
)

st.markdown(
    "- [NHS — Blood Tests]"
    "(https://www.nhs.uk/conditions/blood-tests/)"
)

st.caption(
    "External resources are provided for further learning. "
    "HealthLens AI does not replace professional medical advice."
)

st.divider()

st.caption(
    "HealthLens AI | Health education, not medical diagnosis"
)


