import streamlit as st
# from openai import api_key, base_url

from utills import generater_video_script
st.title("🎬视频脚本生成器")
with st.sidebar:
    api_key=st.text_input("请输入API Key",type="password")
    base_url=st.text_input("请输入API Base URL")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")
    st.markdown("[右键复制OpenAI Base URL](https://api.openai.com/v1/chat/completions)")
subject=st.text_input("💡请输入视频的主题")
video_lenght=st.number_input("🕤请输入视频的大致时长（单位：分钟）",
                             min_value=0.1,max_value=200.0,step=0.1)
creativity=st.slider("✨请输入视频脚本的创造力（数值越小越严谨，数值越大越有创造性）",
                     min_value=0.0,max_value=1.3,step=0.1,value=0.3)
submit=st.button("生成脚本")
if submit and not api_key:
    st.info("请输入API Key")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit and not base_url:
    st.info("请输入Base URL")
    st.stop()
if submit:
    with st.spinner("AI正在思考，请稍等......"):
        statusid,search_result,script,title=generater_video_script(subject,video_lenght,creativity, api_key, base_url)
        # statusid=0
    if statusid==0 or statusid==3:
        st.success("视频脚本已经生成！")
        st.subheader("🔥标题：")
        st.write(title)
        st.subheader("📝视频脚本：")
        st.write(script)
        with st.expander("维基百科搜索结果 👀"):
            st.info(search_result)
    if statusid==3:
        st.info("wiki百科不可用，网络问题")
    if statusid==1:
        st.info("API Key错误或Base URL错误")
    if statusid==4:
        st.info("wiki百科不可用，网络问题，并且API Key错误或Base URL错误")

