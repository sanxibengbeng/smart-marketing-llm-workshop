import streamlit as st
import boto3
import json

st.set_page_config(
    page_title="Marketing Note",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 创建Amazon Bedrock Runtime客户端
client = boto3.client("bedrock-runtime", region_name="us-east-1")


# 定义翻译函数
def translate(model_id, text, target_lang):
    # Set the model ID, e.g., Claude 3 Haiku.

    # Define the prompt for the model.
    prompt = f"translate the text {text} to languate {target_lang}"

    # Format the request payload using the model's native structure.
    native_request = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.5,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    }

    request = json.dumps(native_request)

    # 调用模型并获取响应流
    streaming_response = client.invoke_model_with_response_stream(
        modelId=model_id, body=request
    )

    for event in streaming_response["body"]:
        chunk = json.loads(event["chunk"]["bytes"])
        if chunk["type"] == "content_block_delta":
            chunk_text = chunk["delta"].get("text", "")
            yield chunk_text


# Streamlit应用
def app():
    # 创建两列
    col1, col2 = st.columns(2)

    with col1:
        # 输入文本
        st.markdown("**Source TEXT:**")
        text = st.text_area("", height=200)

        model_id = st.selectbox("Model", ["anthropic.claude-3-haiku-20240307-v1:0", "anthropic.claude-3-5-sonnet-20240620-v1:0"])
        # 选择目标语言
        target_lang = st.selectbox("Target", ["中文", "English", "français", "español", "Deutsch", "日本語", "한국어"])
        btn_clicked = st.button("Translate")

    with col2:
        # 翻译文本
        st.markdown(f"**{target_lang}:**")
        result_container = st.container()
        if btn_clicked:
            with result_container:
                st.markdown("""
                    <style>
                    .result-container {
                        border: 1px solid #ccc;
                        padding: 10px;
                        border-radius: 5px;
                    }
                    </style>
                """, unsafe_allow_html=True)
                st.write_stream(translate(model_id, text, target_lang))


if __name__ == "__main__":
    app()
