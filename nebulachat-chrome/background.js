chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "sendToNebula",
    title: "Send to NebulaChat",
    contexts: ["selection"]
  });
});
chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "sendToNebula") {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      function: () => console.log("Send this to NebulaChat:", window.getSelection().toString())
    });
  }
});